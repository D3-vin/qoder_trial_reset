import json
import uuid
import hashlib
import os
from pathlib import Path
import psutil
import sys
import shutil
from datetime import datetime, timedelta
import platform
import random
import signal

# Rich imports for beautiful UI
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich import box
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.status import Status
from rich.live import Live
from rich.columns import Columns

class QoderStatusChecker:
    def __init__(self):
        self.console = Console()
    
    def log(self, message, style="white"):
        """Print log message using Rich console with styling"""
        if message.startswith("---"):
            # Section headers
            self.console.print(Panel(message.replace("-", "").strip(), 
                                   border_style="bright_blue", 
                                   box=box.SIMPLE))
        elif "✅" in message:
            # Success messages
            self.console.print(message, style="green")
        elif "❌" in message:
            # Error messages  
            self.console.print(message, style="red")
        elif "⚠️" in message:
            # Warning messages
            self.console.print(message, style="yellow")
        elif "🚀" in message or "🎉" in message:
            # Special messages
            self.console.print(Panel(message, border_style="bright_magenta", box=box.DOUBLE))
        elif message.startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.")):
            # Numbered steps
            self.console.print(f"[bold cyan]{message}[/bold cyan]")
        else:
            # Regular messages
            self.console.print(message, style=style)
    
    def create_backup(self, file_path):
        """Create backup of a file or directory with timestamp"""
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                self.log(f"   ⚠️  File {file_path} does not exist, skipping backup")
                return None
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dir = file_path.parent / "backup"
            backup_dir.mkdir(exist_ok=True)
            
            if file_path.is_dir():
                # For directories, create a backup directory
                backup_filename = f"{file_path.name}_{timestamp}"
                backup_path = backup_dir / backup_filename
                shutil.copytree(file_path, backup_path)
                self.log(f"   ✅ Directory backup created: {backup_path}")
            else:
                # For files, create a backup file
                backup_filename = f"{file_path.stem}_{timestamp}{file_path.suffix}"
                backup_path = backup_dir / backup_filename
                shutil.copy2(file_path, backup_path)
                self.log(f"   ✅ File backup created: {backup_path}")
            
            return backup_path
            
        except Exception as e:
            self.log(f"   ❌ Failed to create backup: {e}")
            return None
    
    def check_qoder_running(self):
        """Check if Qoder process is running"""
        pids = []
        is_running = False
        
        # Check for Qoder processes
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if 'qoder' in proc.info['name'].lower():
                    is_running = True
                    pids.append(str(proc.info['pid']))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
                
        return is_running, pids

    def initialize_status_check(self):
        """Initialize and check various statuses"""
        try:
            # 1. Check Qoder process status
            self.log("1. Checking Qoder process status...")
            is_running, pids = self.check_qoder_running()
            if is_running:
                self.log(f"   ✅ Qoder is running (PID: {', '.join(pids)})")
            else:
                self.log("   ✅ Qoder is not running")

            # 2. Check Qoder directory
            self.log("2. Checking Qoder directory...")
            home_dir = Path.home()
            # Adjusting path for cross-platform compatibility
            if sys.platform == "win32":
                qoder_support_dir = home_dir / "AppData/Roaming/Qoder"
            else:
                qoder_support_dir = home_dir / "Library/Application Support/Qoder"

            if qoder_support_dir.exists():
                self.log("   ✅ Qoder directory exists")

                # 3. Check machine ID file
                self.log("3. Checking machine ID file...")
                machine_id_file = qoder_support_dir / "machineid"
                if machine_id_file.exists():
                    try:
                        with open(machine_id_file, 'r') as f:
                            current_id = f.read().strip()
                        self.log(f"   ✅ Machine ID: {current_id}")
                    except Exception as e:
                        self.log(f"   ❌ Failed to read machine ID: {e}")
                else:
                    self.log("   ❌ Machine ID file does not exist")

                # 4. Check telemetry data file
                self.log("4. Checking telemetry data file...")
                storage_json_file = qoder_support_dir / "User/globalStorage/storage.json"
                if storage_json_file.exists():
                    try:
                        with open(storage_json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)

                        if 'telemetry.machineId' in data:
                            machine_id = data['telemetry.machineId']
                            self.log(f"   ✅ Telemetry machine ID: {machine_id[:16]}...")
                        else:
                            self.log("   ⚠️  Telemetry machine ID not found")

                        if 'telemetry.devDeviceId' in data:
                            device_id = data['telemetry.devDeviceId']
                            self.log(f"   ✅ Device ID: {device_id}")
                        else:
                            self.log("   ⚠️  Device ID not found")

                    except Exception as e:
                        self.log(f"   ❌ Failed to read telemetry data: {e}")
                else:
                    self.log("   ❌ Telemetry data file does not exist")
            else:
                self.log("   ❌ Qoder directory does not exist")
                
        except Exception as e:
            self.log(f"   ❌ Error during status check: {e}")

    def reset_machine_id(self):
        """Reset machine ID"""
        self.log("Starting machine ID reset...")

        # Check if Qoder is running
        is_running, _ = self.check_qoder_running()
        if is_running:
            self.log("Error: Qoder is running, please close it first")
            # QMessageBox.critical(self, "Error", "Please close the Qoder application first")
            return

        try:
            home_dir = Path.home()
            # Adjusting path for cross-platform compatibility
            if sys.platform == "win32":
                qoder_support_dir = home_dir / "AppData/Roaming/Qoder"
            else:
                qoder_support_dir = home_dir / "Library/Application Support/Qoder"
            machine_id_file = qoder_support_dir / "machineid"

            if not qoder_support_dir.exists():
                raise Exception("Qoder application data directory not found")

            if machine_id_file.exists():
                # Create backup before modifying
                self.log("Creating backup of machine ID file...")
                backup_path = self.create_backup(machine_id_file)
                if backup_path is None:
                    self.log("Warning: Failed to create backup, continuing anyway...")
                
                new_machine_id = str(uuid.uuid4())
                with open(machine_id_file, 'w') as f:
                    f.write(new_machine_id)
                self.log(f"Machine ID has been reset to: {new_machine_id}")
                # QMessageBox.information(self, "Success", "Machine ID reset completed")
            else:
                self.log("Machine ID file not found")
                # QMessageBox.warning(self, "Warning", "Machine ID file not found")

        except Exception as e:
            self.log(f"Failed to reset machine ID: {e}")
            # QMessageBox.critical(self, "Error", f"Failed to reset machine ID: {e}")

    def reset_all_data(self):
        """Reset both machine ID and telemetry data with progress tracking"""
        self.log("Starting complete data reset (Machine ID + Telemetry + Advanced Cleanup)...")

        # Check if Qoder is running
        is_running, _ = self.check_qoder_running()
        if is_running:
            self.log("❌ Error: Qoder is running, please close it first", "red")
            return

        try:
            home_dir = Path.home()
            # Adjusting path for cross-platform compatibility
            if sys.platform == "win32":
                qoder_support_dir = home_dir / "AppData/Roaming/Qoder"
            else:
                qoder_support_dir = home_dir / "Library/Application Support/Qoder"
            
            if not qoder_support_dir.exists():
                raise Exception("Qoder application data directory not found")

            # Progress tracking
            reset_tasks = [
                ("Enhanced Machine ID Reset", self.reset_machine_id_enhanced),
                ("Advanced Telemetry Reset", self.reset_telemetry_enhanced),
                ("Advanced Cache Cleanup", self.advanced_cache_cleanup),
                ("Deep Identity Cleanup", self.deep_identity_cleanup),
                ("Login Identity Cleanup", self.login_identity_cleanup),
                ("Hardware Fingerprint Reset", self.hardware_fingerprint_reset),
                ("Hidden Files Cleanup", lambda qsd: self.cleanup_hidden_and_temp_files(qsd)),
                ("Smart Conversation Management", self.smart_conversation_cleanup)
            ]

            self.log("🚀 STARTING COMPREHENSIVE QODER RESET")
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeElapsedColumn(),
                console=self.console
            ) as progress:
                
                main_task = progress.add_task("🔄 Resetting Qoder Identity...", total=len(reset_tasks))
                
                for i, (task_name, task_func) in enumerate(reset_tasks, 1):
                    progress.update(main_task, description=f"🔧 {task_name}...")
                    
                    self.log(f"\n--- 🔧 {task_name} ---")
                    task_func(qoder_support_dir)
                    
                    progress.advance(main_task)
                    import time
                    time.sleep(0.3)  # Brief pause for visual effect

            self.log("🎉 COMPREHENSIVE RESET COMPLETED SUCCESSFULLY!")
            self.log("✅ All identity data has been reset")
            self.log("✅ Hardware fingerprints have been regenerated")
            self.log("✅ Cache and temporary data cleared")
            self.log("🔄 You can now restart Qoder safely")

        except Exception as e:
            self.log(f"❌ Failed to reset data: {e}", "red")

    def reset_machine_id_enhanced(self, qoder_support_dir):
        """Enhanced machine ID reset with multiple ID files"""
        try:
            # Main machine ID file
            machine_id_file = qoder_support_dir / "machineid"
            new_machine_id = str(uuid.uuid4())
            
            # Create backup if file exists
            if machine_id_file.exists():
                backup_path = self.create_backup(machine_id_file)
                if backup_path:
                    self.log("   ✅ Backup created successfully")
            
            with open(machine_id_file, 'w') as f:
                f.write(new_machine_id)
            self.log(f"   ✅ Main machine ID reset: {new_machine_id}")
            
            # Create additional ID files for enhanced protection
            additional_ids = [
                "deviceid", "hardware_uuid", "system_uuid", 
                "platform_id", "installation_id", "cpu_id", "gpu_id"
            ]
            
            for id_file in additional_ids:
                file_path = qoder_support_dir / id_file
                new_id = str(uuid.uuid4())
                with open(file_path, 'w') as f:
                    f.write(new_id)
                self.log(f"   ✅ Created: {id_file}")
            
        except Exception as e:
            self.log(f"   ❌ Machine ID reset failed: {e}")

    def reset_telemetry_enhanced(self, qoder_support_dir):
        """Enhanced telemetry reset with comprehensive ID generation"""
        try:
            storage_json_file = qoder_support_dir / "User/globalStorage/storage.json"
            
            if storage_json_file.exists():
                # Create backup
                backup_path = self.create_backup(storage_json_file)
                if backup_path:
                    self.log("   ✅ Backup created successfully")
                
                with open(storage_json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Generate comprehensive new telemetry IDs
                new_uuid = str(uuid.uuid4())
                machine_id_hash = hashlib.sha256(new_uuid.encode()).hexdigest()
                
                # Core telemetry identifiers
                telemetry_ids = {
                    'telemetry.machineId': machine_id_hash,
                    'telemetry.devDeviceId': str(uuid.uuid4()),
                    'telemetry.sessionId': str(uuid.uuid4()),
                    'telemetry.installationId': str(uuid.uuid4()),
                    'telemetry.clientId': str(uuid.uuid4()),
                    'telemetry.userId': str(uuid.uuid4()),
                    'telemetry.anonymousId': str(uuid.uuid4()),
                    'telemetry.sqmId': str(uuid.uuid4()),
                    # Backup identifiers
                    'machineId': machine_id_hash,
                    'deviceId': str(uuid.uuid4()),
                    'installationId': str(uuid.uuid4()),
                    'hardwareId': str(uuid.uuid4()),
                    'platformId': str(uuid.uuid4())
                }
                
                # System fingerprint
                system_info = {
                    'system.platform': platform.system().lower(),
                    'system.arch': platform.machine(),
                    'system.version': self.generate_system_version(),
                    'system.timezone': random.choice(['UTC-8', 'UTC-5', 'UTC+0', 'UTC+1', 'UTC+8'])
                }
                
                # Update all identifiers
                data.update(telemetry_ids)
                data.update(system_info)
                
                with open(storage_json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)

                self.log(f"   ✅ Enhanced telemetry reset completed")
                self.log(f"   📊 Updated {len(telemetry_ids)} telemetry IDs")
                self.log(f"   🖥️  Updated {len(system_info)} system fingerprints")
            else:
                self.log("   ⚠️  Telemetry file not found")
                
        except Exception as e:
            self.log(f"   ❌ Telemetry reset failed: {e}")

    def generate_system_version(self):
        """Generate realistic system version based on platform"""
        system_type = platform.system()
        
        if system_type == "Darwin":  # macOS
            major = random.randint(12, 15)
            minor = random.randint(0, 6)
            patch = random.randint(0, 9)
            return f"{major}.{minor}.{patch}"
        elif system_type == "Windows":
            versions = ["10.0.19045", "10.0.22621", "10.0.22631", "10.0.26100"]
            base = random.choice(versions)
            build = random.randint(1, 999)
            return f"{base}.{build}"
        else:  # Linux
            major = random.choice([5, 6])
            minor = random.randint(0, 19) if major == 5 else random.randint(0, 8)
            patch = random.randint(0, 50)
            return f"{major}.{minor}.{patch}"

    def advanced_cache_cleanup(self, qoder_support_dir):
        """Advanced cache cleanup including GPU and specialized caches"""
        try:
            cache_dirs = [
                "Cache", "blob_storage", "Code Cache", "SharedClientCache",
                "GPUCache", "DawnGraphiteCache", "DawnWebGPUCache", "ShaderCache",
                "CachedData", "CachedProfilesData", "CachedExtensions",
                "IndexedDB", "CacheStorage", "WebSQL", "Dictionaries",
                # Enhanced: Additional specialized caches
                "DawnCache", "MediaCache", "MetadataCache", "ThumbnailCache",
                "IndexCache", "SearchCache", "QueryCache", "ResultsCache",
                # Enhanced: Extension and plugin caches
                "ExtensionData", "PluginData", "AddonData",
                "ExtensionPrefs", "PluginPrefs", "AddonPrefs",
                "CachedExtensionVSIXs",
                # Enhanced: WebKit and Chromium caches
                "WebKitCache", "WebProcessCache", "PluginProcessCache",
                "RenderProcessCache", "GPUProcessCache",
                "ChromiumState", "ChromiumPrefs", "ChromiumHistory",
                "ChromiumCookies", "ChromiumSessions"
            ]

            cleaned = 0
            for cache_dir in cache_dirs:
                cache_path = qoder_support_dir / cache_dir
                if cache_path.exists():
                    try:
                        # Special handling for SharedClientCache to preserve MCP files
                        if cache_dir == "SharedClientCache":
                            self.clean_shared_client_cache_selective(cache_path)
                            self.log(f"   ✅ Selectively cleared: {cache_dir} (MCP preserved)")
                            cleaned += 1
                        else:
                            # Create backup before deletion for other caches
                            backup_path = self.create_backup(cache_path)
                            if backup_path:
                                self.log(f"   📋 Backup created for: {cache_dir}")
                            
                            shutil.rmtree(cache_path)
                            self.log(f"   ✅ Cleared: {cache_dir}")
                            cleaned += 1
                    except Exception as e:
                        self.log(f"   ⚠️  Failed to clear {cache_dir}: {e}")

            self.log(f"   🧹 Cleared {cleaned}/{len(cache_dirs)} cache directories")
            
        except Exception as e:
            self.log(f"   ❌ Cache cleanup failed: {e}")

    def deep_identity_cleanup(self, qoder_support_dir):
        """Deep cleanup of identity-related files and network state"""
        try:
            # Network and identity files
            identity_files = [
                "Network Persistent State", "TransportSecurity", "Trust Tokens",
                "Trust Tokens-journal", "SharedStorage", "SharedStorage-wal",
                "Preferences", "Secure Preferences", "Local State",
                "DeviceMetadata", "HardwareInfo", "SystemInfo",
                "QuotaManager", "QuotaManager-journal", "origin_bound_certs",
                "Cookies", "Cookies-journal", "Web Data", "Web Data-journal",
                "cert_transparency_reporter_state.json",
                # Enhanced: Additional browser fingerprint files
                "BrowserUserAgent", "ClientHints", "NavigatorInfo",
                "ScreenInfo", "TimezoneInfo", "LanguageInfo",
                # Enhanced: More network files
                "DNSCache", "HTTPCache", "ProxySettings",
                "NetworkConfiguration", "ConnectionHistory",
                "NetworkDataMigrated", "Reporting and NEL", "HSTS",
                # Enhanced: Security and authentication
                "SecuritySettings", "CertificateStore", "TrustStore",
                "EncryptionKeys", "AuthTokens", "SessionKeys",
                "Certificate Revocation Lists", "SSLCertificates",
                # Enhanced: User activity tracking
                "UserActivity", "AppUsage", "FeatureUsage",
                "InteractionHistory", "AccessLog", "AuditLog",
                "ActivityLog", "EventLog", "UserActivityLog",
                # Enhanced: Autofill and form data
                "AutofillStrikeDatabase", "AutofillStrikeDatabase-journal",
                "Feature Engagement Tracker", "PasswordStoreDefault",
                "AutofillRegexes", "PreferredApps", "UserPrefs", "UserPrefs.backup",
                # Enhanced: Browser metrics and telemetry
                "BrowserMetrics", "SafeBrowsing", "OriginTrials",
                "VideoDecodeStats", "Platform Notifications",
                # Enhanced: Search and history
                "Visited Links", "History", "History-journal",
                "Favicons", "Favicons-journal", "Shortcuts", "Shortcuts-journal",
                "Top Sites", "Top Sites-journal"
            ]
            
            cleaned = 0
            for identity_file in identity_files:
                file_path = qoder_support_dir / identity_file
                if file_path.exists():
                    try:
                        # Create backup before deletion
                        backup_path = self.create_backup(file_path)
                        if backup_path:
                            self.log(f"   📋 Backup created for: {identity_file}")
                        
                        if file_path.is_dir():
                            shutil.rmtree(file_path)
                        else:
                            file_path.unlink()
                        self.log(f"   ✅ Removed: {identity_file}")
                        cleaned += 1
                    except Exception as e:
                        self.log(f"   ⚠️  Failed to remove {identity_file}: {e}")

            # Clean storage directories
            storage_dirs = [
                "Session Storage", "Local Storage", "WebStorage",
                "Shared Dictionary", "Service Worker", "databases"
            ]
            
            for storage_dir in storage_dirs:
                storage_path = qoder_support_dir / storage_dir
                if storage_path.exists():
                    try:
                        # Create backup before deletion
                        backup_path = self.create_backup(storage_path)
                        if backup_path:
                            self.log(f"   📋 Backup created for: {storage_dir}")
                        
                        shutil.rmtree(storage_path)
                        self.log(f"   ✅ Cleared: {storage_dir}")
                        cleaned += 1
                    except Exception as e:
                        self.log(f"   ⚠️  Failed to clear {storage_dir}: {e}")

            self.log(f"   🔥 Deep cleanup completed: {cleaned} items processed")
            
        except Exception as e:
            self.log(f"   ❌ Deep identity cleanup failed: {e}")

    def login_identity_cleanup(self, qoder_support_dir):
        """Cleanup login and authentication related data"""
        try:
            # Clean SharedClientCache login files (preserve mcp.json)
            shared_cache = qoder_support_dir / "SharedClientCache"
            if shared_cache.exists():
                # Clear only auth-related files, preserve MCP configuration
                login_files = [".info", ".lock", "auth.json", "server.json"]
                for file_name in login_files:
                    file_path = shared_cache / file_name
                    if file_path.exists():
                        try:
                            file_path.unlink()
                            self.log(f"   ✅ Cleared: SharedClientCache/{file_name}")
                        except Exception as e:
                            self.log(f"   ⚠️  Failed to clear {file_name}: {e}")
                
                # Preserve mcp.json files - important MCP configuration
                mcp_files = [
                    shared_cache / "mcp.json",
                    shared_cache / "extension" / "local" / "mcp.json"
                ]
                
                for mcp_file in mcp_files:
                    if mcp_file.exists():
                        self.log(f"   💾 Preserved: {mcp_file.relative_to(qoder_support_dir)} (MCP config)")
                
                self.log("   ℹ️  MCP configuration files preserved for functionality")

            # Clean authentication files
            auth_files = [
                "Login Credentials", "Login Data", "Login Data-journal",
                "AutofillStrikeDatabase", "AutofillStrikeDatabase-journal",
                "Feature Engagement Tracker", "PasswordStoreDefault"
            ]
            
            for auth_file in auth_files:
                file_path = qoder_support_dir / auth_file
                if file_path.exists():
                    try:
                        if file_path.is_dir():
                            shutil.rmtree(file_path)
                        else:
                            file_path.unlink()
                        self.log(f"   ✅ Cleared: {auth_file}")
                    except Exception as e:
                        self.log(f"   ⚠️  Failed to clear {auth_file}: {e}")

            # Clean login-related configs from storage.json
            storage_file = qoder_support_dir / "User/globalStorage/storage.json"
            if storage_file.exists():
                try:
                    with open(storage_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    login_keys = [key for key in data.keys() if any(keyword in key.lower() 
                                 for keyword in ['login', 'auth', 'token', 'credential', 'session'])]
                    
                    for key in login_keys:
                        del data[key]
                        self.log(f"   ✅ Cleared config: {key}")
                    
                    if login_keys:
                        with open(storage_file, 'w', encoding='utf-8') as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
                    
                except Exception as e:
                    self.log(f"   ⚠️  Failed to clean configs: {e}")

            self.log("   🔐 Login identity cleanup completed")
            
        except Exception as e:
            self.log(f"   ❌ Login cleanup failed: {e}")

    def hardware_fingerprint_reset(self, qoder_support_dir):
        """Reset hardware fingerprints and generate fake hardware info"""
        try:
            system_type = platform.system()
            
            # Generate fake hardware info based on system
            if system_type == "Darwin":  # macOS
                fake_hardware = {
                    "cpu": {
                        "name": f"Apple M{random.randint(2, 5)} Pro",
                        "cores": random.choice([8, 10, 12, 16]),
                        "frequency": f"{random.uniform(2.0, 4.0):.1f}GHz"
                    },
                    "gpu": {
                        "name": f"Apple M{random.randint(2, 5)} Pro GPU",
                        "memory": f"{random.choice([16, 24, 32])}GB"
                    },
                    "memory": {
                        "total": f"{random.choice([16, 24, 32, 64])}GB",
                        "type": "LPDDR5"
                    }
                }
            elif system_type == "Windows":
                cpu_brands = ["Intel", "AMD"]
                gpu_brands = ["NVIDIA", "AMD", "Intel"]
                fake_hardware = {
                    "cpu": {
                        "name": f"{random.choice(cpu_brands)} Core i{random.choice([5,7,9])}-{random.randint(12000,14000)}",
                        "cores": random.choice([6, 8, 12, 16]),
                        "frequency": f"{random.uniform(3.0, 5.0):.1f}GHz"
                    },
                    "gpu": {
                        "name": f"{random.choice(gpu_brands)} RTX {random.choice([4060, 4070, 4080])}",
                        "memory": f"{random.choice([8, 12, 16])}GB"
                    },
                    "memory": {
                        "total": f"{random.choice([16, 32, 64])}GB",
                        "type": "DDR5"
                    }
                }
            else:  # Linux
                fake_hardware = {
                    "cpu": {
                        "name": f"Intel Core i{random.choice([5,7])}-{random.randint(10000,12000)}",
                        "cores": random.choice([4, 6, 8]),
                        "frequency": f"{random.uniform(2.5, 4.0):.1f}GHz"
                    },
                    "gpu": {
                        "name": f"NVIDIA GTX {random.choice([1650, 1660, 3060])}",
                        "memory": f"{random.choice([4, 6, 8])}GB"
                    },
                    "memory": {
                        "total": f"{random.choice([8, 16, 32])}GB",
                        "type": "DDR4"
                    }
                }
            
            # Add system info
            fake_hardware.update({
                "system": {
                    "platform": system_type.lower(),
                    "version": self.generate_system_version(),
                    "arch": platform.machine()
                },
                "fingerprint_reset": {
                    "timestamp": datetime.now().isoformat(),
                    "reset_id": str(uuid.uuid4())
                }
            })
            
            # Create multiple fake hardware files
            fake_files = [
                "hardware_detection.json", "device_capabilities.json", 
                "system_features.json", "platform_detection.json"
            ]
            
            for fake_file in fake_files:
                file_path = qoder_support_dir / fake_file
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(fake_hardware, f, indent=2, ensure_ascii=False)
                self.log(f"   ✅ Created: {fake_file}")
            
            # Clear existing hardware cache
            hardware_dirs = ["GPUCache", "DawnGraphiteCache", "DawnWebGPUCache", "ShaderCache"]
            for hw_dir in hardware_dirs:
                dir_path = qoder_support_dir / hw_dir
                if dir_path.exists():
                    try:
                        shutil.rmtree(dir_path)
                        self.log(f"   ✅ Cleared: {hw_dir}")
                    except Exception as e:
                        self.log(f"   ⚠️  Failed to clear {hw_dir}: {e}")
            
            self.log(f"   🛡️ Hardware fingerprint reset completed for {system_type}")
            
            # Create decoy files to confuse detection systems
            self.create_decoy_files(qoder_support_dir)
            
        except Exception as e:
            self.log(f"   ❌ Hardware reset failed: {e}")
    
    def create_decoy_files(self, qoder_support_dir):
        """Create decoy files to confuse detection systems"""
        try:
            self.log("   Creating decoy files for detection confusion...")
            
            decoy_files = [
                "real_machine_id.tmp", "backup_device_id.log", 
                "old_telemetry.dat", "previous_session.cache",
                "legacy_fingerprint.json", "archived_identity.bak",
                "system_backup.tmp", "device_clone.dat",
                "hardware_backup.json", "original_config.bak"
            ]
            
            for decoy_file in decoy_files:
                file_path = qoder_support_dir / decoy_file
                fake_data = {
                    "fake_id": str(uuid.uuid4()),
                    "timestamp": (datetime.now() - timedelta(days=random.randint(30, 365))).isoformat(),
                    "data": hashlib.md5(str(random.random()).encode()).hexdigest(),
                    "note": "Legacy backup file",
                    "version": f"{random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                }
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(fake_data, f, indent=2)
                
                self.log(f"   ✅ Created decoy: {decoy_file}")
            
        except Exception as e:
            self.log(f"   ⚠️  Decoy creation failed: {e}")

    def smart_conversation_cleanup(self, qoder_support_dir):
        """Smart conversation management - preserve important data"""
        try:
            # For now, we preserve conversations by default
            # Users can manually delete if needed
            conversation_dirs = [
                "User/workspaceStorage", "User/History", "logs"
            ]
            
            preserved = 0
            for conv_dir in conversation_dirs:
                dir_path = qoder_support_dir / conv_dir
                if dir_path.exists():
                    preserved += 1
            
            if preserved > 0:
                self.log(f"   💬 Preserved {preserved} conversation-related directories")
                self.log("   ℹ️  Conversations preserved by default")
            else:
                self.log("   ℹ️  No conversation data found")
            
        except Exception as e:
            self.log(f"   ❌ Conversation management failed: {e}")
    
    def cleanup_hidden_and_temp_files(self, qoder_support_dir):
        """Clean up hidden files and temporary files"""
        try:
            self.log("   Cleaning hidden and temporary files...")
            cleaned = 0
            
            # Clean hidden files (starting with .)
            for root, dirs, files in os.walk(qoder_support_dir):
                # Clean hidden files
                for file in files:
                    if file.startswith('.') and file not in ['.gitignore', '.gitkeep']:
                        file_path = Path(root) / file
                        try:
                            file_path.unlink()
                            self.log(f"   ✅ Cleaned hidden file: {file}")
                            cleaned += 1
                        except Exception as e:
                            self.log(f"   ⚠️  Failed to clean {file}: {e}")
                
                # Clean hidden directories
                for dir_name in dirs[:]:
                    if dir_name.startswith('.') and dir_name not in ['.git']:
                        dir_path = Path(root) / dir_name
                        try:
                            shutil.rmtree(dir_path)
                            self.log(f"   ✅ Cleaned hidden directory: {dir_name}")
                            dirs.remove(dir_name)
                            cleaned += 1
                        except Exception as e:
                            self.log(f"   ⚠️  Failed to clean {dir_name}: {e}")
            
            # Clean temporary files by extension
            temp_extensions = ['.tmp', '.temp', '.cache', '.lock', '.pid']
            for root, dirs, files in os.walk(qoder_support_dir):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in temp_extensions):
                        file_path = Path(root) / file
                        try:
                            file_path.unlink()
                            self.log(f"   ✅ Cleaned temp file: {file}")
                            cleaned += 1
                        except Exception as e:
                            self.log(f"   ⚠️  Failed to clean {file}: {e}")
            
            self.log(f"   🧹 Hidden/temp cleanup completed: {cleaned} files")
            
        except Exception as e:
            self.log(f"   ❌ Hidden/temp cleanup failed: {e}")
    
    def clean_shared_client_cache_selective(self, shared_cache_path):
        """Selectively clean SharedClientCache while preserving MCP configuration files"""
        try:
            # Define MCP files to preserve
            mcp_files_to_preserve = [
                "mcp.json",
                "extension/local/mcp.json"
            ]
            
            # Create backup of the entire directory first
            backup_path = self.create_backup(shared_cache_path)
            if backup_path:
                self.log(f"   📋 Full backup created for SharedClientCache")
            
            # Clean everything except MCP files
            for item in shared_cache_path.rglob('*'):
                if item.is_file():
                    # Check if this file should be preserved
                    relative_path = item.relative_to(shared_cache_path)
                    should_preserve = any(str(relative_path) == mcp_file or 
                                        str(relative_path).endswith(mcp_file) 
                                        for mcp_file in mcp_files_to_preserve)
                    
                    if not should_preserve:
                        try:
                            item.unlink()
                            self.log(f"   ✅ Cleaned: SharedClientCache/{relative_path}")
                        except Exception as e:
                            self.log(f"   ⚠️  Failed to clean {relative_path}: {e}")
                    else:
                        self.log(f"   💾 Preserved: SharedClientCache/{relative_path} (MCP config)")
            
            # Clean empty directories (but preserve structure for MCP)
            for item in shared_cache_path.rglob('*'):
                if item.is_dir() and not any(item.iterdir()):
                    # Don't remove directories that might be needed for MCP
                    if "extension" not in str(item.relative_to(shared_cache_path)):
                        try:
                            item.rmdir()
                            self.log(f"   ✅ Removed empty dir: {item.relative_to(shared_cache_path)}")
                        except Exception:
                            pass  # Directory not empty or protected
            
        except Exception as e:
            self.log(f"   ❌ Selective SharedClientCache cleanup failed: {e}")

def display_menu():
    """Display the simplified main menu with Rich styling"""
    console = Console()
    
    # Clear screen and show title
    console.clear()
    
    # Create combined title and social links
    combined_text = Text()
    
    # Add social links in column format
    combined_text.append("\n📢 Channel: ", style="bold white")
    combined_text.append("https://t.me/D3_vin", style="cyan")
    combined_text.append("\n")
    combined_text.append("💬 Chat: ", style="bold white")
    combined_text.append("https://t.me/D3vin_chat", style="cyan")
    combined_text.append("\n")
    combined_text.append("📁 GitHub: ", style="bold white")
    combined_text.append("https://github.com/D3-vin", style="cyan")
    combined_text.append("\n")
    combined_text.append("📁 Version: ", style="bold white")
    combined_text.append("1.1", style="green")
    
    # Add line break and title
    combined_text.append("\n")
    #combined_text.append("🚀 QODER RESET TOOL 🚀", style="bold magenta")
    
    # Combined panel with same style as menu
    title_panel = Panel(
        Align.left(combined_text),
        title="[bold blue]🚀 QODER RESET TOOL 🚀[/bold blue]",  # Added title
        subtitle="[bold magenta]Dev by D3vin[/bold magenta]",  # Added subtitle at bottom
        box=box.ROUNDED,  # Same as menu
        border_style="bright_blue",  # Same color as menu
        padding=(0, 1),
        width=70  # Same width as menu
    )
    
    console.print(title_panel)
    console.print()
    
    # Create simple menu table with limited width
    table = Table(
        show_header=False,
        box=None,
        border_style="bright_blue",
        expand=False,  # Don't expand to full width
        width=65,  # Smaller fixed width
        padding=(0, 2)
    )
    
    table.add_column("Menu Options", style="white", justify="left")
    
    # Simple menu options with numbers and descriptions combined
    table.add_row(
        "[bold bright_green]🔍 1[/bold bright_green] [bold bright_green]CHECK[/bold bright_green] - Comprehensive system status analysis"
    )
    
    table.add_row(
        "[bold bright_yellow]🔄 2[/bold bright_yellow] [bold bright_yellow]RESET[/bold bright_yellow] - Complete advanced reset (All Features)"
    )
    
    table.add_row(
        "[bold bright_red]🚪 3[/bold bright_red] [bold bright_red]EXIT[/bold bright_red] - Close application"
    )
    
    # Menu panel - with limited width
    menu_panel = Panel(
        table,
        title="[bold blue]📋 Menu[/bold blue]",
        border_style="bright_blue",
        padding=(0, 1),
        width=70  # Smaller width
    )
    
    console.print(menu_panel)

def graceful_exit(console):
    """Graceful exit function for Ctrl+C handling"""
    console.print("\n[bold bright_blue]👋 Goodbye![/bold bright_blue]")
    sys.exit(0)

def signal_handler(signum, frame):
    """Handle Ctrl+C signal"""
    console = Console()
    graceful_exit(console)

def main():
    """Main function with simplified Rich menu system"""
    checker = QoderStatusChecker()
    console = Console()
    
    # Setup signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    while True:
        display_menu()
        console.print()
        
        # Use Rich prompt for better input
        choice = Prompt.ask(
            "[bold bright_white]Choose option[/bold bright_white]",
            choices=["1", "2", "3"],
            default="1"
        )
        
        if choice == "1":
            # Status check
            console.print("\n[bold bright_green]🔍 Checking status...[/bold bright_green]\n")
            checker.initialize_status_check()
            
        elif choice == "2":
            # Reset with confirmation
            console.print("\n[bold bright_yellow]⚠️  This will reset all Qoder identity data![/bold bright_yellow]")
            confirm = Prompt.ask(
                "[bold red]Continue?[/bold red]",
                choices=["y", "n"],
                default="n"
            )
            
            if confirm.lower() == "y":
                console.print("\n[bold bright_red]🔄 Resetting...[/bold bright_red]\n")
                checker.reset_all_data()
            else:
                console.print("[yellow]Cancelled.[/yellow]")
                
        elif choice == "3":
            # Exit
            graceful_exit(console)
        
        # Pause
        if choice in ["1", "2"]:
            console.print()
            Prompt.ask("[dim]Press Enter to continue...[/dim]", default="")

if __name__ == "__main__":
    main()