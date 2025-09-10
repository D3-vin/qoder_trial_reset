# 🚀 Advanced Qoder Reset Tool

> **🌐 Language**: [Русский](README_RUS.md) | **English**

A comprehensive command-line tool for cleaning Qoder application detectable files and changing machine IDs with advanced anti-detection features and configuration management.

## 📢 Connect with Us

- **📢 Channel**: [https://t.me/D3_vin](https://t.me/D3_vin) - Latest updates and releases
- **💬 Chat**: [https://t.me/D3vin_chat](https://t.me/D3vin_chat) - Community support and discussions
- **📁 GitHub**: [https://github.com/D3-vin](https://github.com/D3-vin) - Source code and development

![Python](https://img.shields.io/badge/Python-3.6+-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-Educational%20Use-green)

**✨ Important Note: After resetting Qoder, please use a fingerprint-protected browser for registration to avoid detection of duplicate registration due to browser cache or fingerprints. The author has been using it for 2 days after reset.**

**Like Cursor and Augment, subsequent detection will become increasingly strict. No guarantee how long it will work - use it while you can.**

## Version 0.1.23

## 📋 Table of Contents

- [Key Features](#key-features)
- [System Requirements](#system-requirements)
- [Quick Installation](#quick-installation)
- [Usage Guide](#usage-guide)
- [Technical Details](#technical-details)
- [File Operations](#file-operations)
- [Safety Features](#safety-features)
- [Troubleshooting](#troubleshooting)

## ✨ Key Features

### 🛡️ Advanced Anti-Detection System
- **🧹 Deep File Cleanup** - Remove detectable files while preserving important data
- **📊 Telemetry Data Cleanup** - Clear comprehensive telemetry and device tracking data
- **🔥 Identity File Cleanup** - Remove network states, trust tokens, and local storage
- **🔐 Login Identity Cleanup** - Clear authentication tokens and session data
- **🛡️ Hardware Fingerprint Cleanup** - Remove hardware detection files
- **💬 Smart Data Preservation** - Preserve MCP settings and chat history
- **🧹 Advanced Cache Cleanup** - Clear application caches while protecting important data
- **⚡ Live Machine ID Change** - Change machine ID while Qoder is running (requires administrator privileges)

### 🔒 Safety & Configuration System
- **⚙️ Configuration Management** - JSON-based configuration for runtime behavior
- **🔍 Process Detection** - Detects Qoder running status for safe operations
- **💾 Data Preservation** - Preserves MCP settings and conversation data
- **🔄 Graceful Error Handling** - Continues operation even if individual operations fail
- **📝 Comprehensive Logging** - Detailed operation logs with status indicators
- **🎯 Selective Cleanup** - Only removes detectable files, preserves functionality

### 🌍 Cross-Platform Support
- **Windows 10/11** - Full feature support (`%APPDATA%\Qoder`)
- **macOS 12+** - Complete compatibility (`~/Library/Application Support/Qoder`)
- **Linux** - Basic support with fallback paths

## 🖥️ System Requirements

- **Operating System**: Windows 10+, macOS 12+, or Linux
- **Python**: 3.6 or higher
- **Dependencies**: `psutil`, `rich`
- **Disk Space**: At least 100MB free space
- **Permissions**: 
  - Windows: Read/write access to `%APPDATA%\Qoder`
  - macOS: Read/write access to `~/Library/Application Support/Qoder`
  - Linux: Read/write access to user application data directory

## 📦 Quick Installation

### Method 1: Automatic Installation (Recommended)

```bash
# Using requirements.txt
pip install -r requirements.txt
python main.py
```

### Method 2: Platform-Specific Installers

**Windows:**
```cmd
install.bat
```

**macOS/Linux:**
```bash
chmod +x install.sh
./install.sh
```

**Python Installer:**
```bash
python install.py
```

### Method 3: Manual Installation

```bash
# 1. Clone or download the repository
git clone <repository-url>
cd qoder-reset

# 2. Install dependencies
pip install psutil rich

# 3. Run the tool
python main.py
```

### Method 4: One-Command Setup

```bash
# Install and run in one go
pip install psutil rich && python main.py
```

## 🚀 Usage Guide

### Basic Usage Flow

1. **Start Application**: `python main.py`
2. **Check Status**: Choose option 1 to analyze current system state
3. **Execute Reset**: Choose option 2 for comprehensive reset
4. **Monitor Progress**: Watch detailed logs for operation status
5. **Restart Qoder**: Launch Qoder to verify new identity

### Menu Options

```
🚀 QODER RESET TOOL 🚀
═══════════════════════════════════════════════════════════
🔍 1. CHECK - Comprehensive system status analysis
   • Process status • File integrity • Configuration status

🧹 2. CLEANUP - Delete detectable files
   ✅ Telemetry Data Cleanup
   ✅ Deep Identity & Network State Cleanup  
   ✅ Advanced Cache & Storage Cleanup
   ✅ Hardware Fingerprint Cleanup
   ✅ Login Identity & Authentication Cleanup
   ✅ Smart Data Preservation (MCP settings & chats)

⚡ 3. CHANGE MACHINE_ID - Live machine ID modification
   ✅ Real-time machine ID change while Qoder runs
   ✅ Create new or use saved machine IDs
   ⚠️  Requires Qoder to be running and administrator privileges

🚪 4. EXIT - Close application
═══════════════════════════════════════════════════════════
💡 Tip: Run CHECK first to see current system status
```

### Quick Start Example

```bash
# 1. Run the tool
python main.py

# 2. Choose option 1 to check current status
1

# 3. Choose option 2 to cleanup detectable files
2

# 4. Or choose option 3 to change machine ID (Qoder must be running)
3

# 5. Monitor the detailed progress logs
# 6. Choose option 4 to exit when done
4
```

## 🔧 Technical Details

### Architecture Overview

The tool implements a comprehensive cleanup and live modification system:

**Cleanup Mode (Option 2):**
1. **🧹 Machine ID Cleanup** - Remove additional machine identifier files
2. **📊 Telemetry Data Cleanup** - Remove telemetry identifiers from storage
3. **🧹 Advanced Cache Cleanup** - Clear 15+ cache directories
4. **🔥 Deep Identity Cleanup** - Remove network and authentication files
5. **🔐 Login Identity Cleanup** - Clear login credentials and session data
6. **🛡️ Hardware Fingerprint Cleanup** - Remove hardware detection files
7. **💬 Smart Data Preservation** - Preserve MCP settings and conversation data

**Live Machine ID Change (Option 3):**
- **⚡ Real-time Modification** - Change machine ID while Qoder is running
- **💾 ID Management** - Create new or use saved machine IDs
- **🔧 Memory Injection** - Direct memory modification using pymem
- **⚠️ Administrator Required** - Needs elevated privileges for memory access

### Core Technologies

- **Process Detection**: Cross-platform process monitoring with `psutil`
- **Rich Interface**: Beautiful CLI with colors, tables, and progress bars using `rich`
- **File Operations**: Safe file handling with `pathlib` and `shutil`
- **JSON Processing**: Configuration file manipulation with built-in `json` module
- **UUID Generation**: Cryptographically secure identifiers with `uuid.uuid4()`
- **Memory Injection**: Real-time memory modification with `pymem` for live ID changes
- **Configuration Management**: Runtime behavior control through `config.json`
- **Modular Architecture**: Separated machine ID functionality for code protection

## 📁 File Operations

### Files Created/Modified

#### 🔑 **Machine Identity Files (Cleaned/Managed)**
```
📄 machineid                    - Primary machine UUID (preserved, managed by machine_id_changer)
📄 deviceid                     - Device identifier (removed if exists)
📄 hardware_uuid                - Hardware-specific UUID (removed if exists)
📄 system_uuid                  - System identifier (removed if exists)
📄 platform_id                  - Platform-specific ID (removed if exists)
📄 installation_id              - Installation UUID (removed if exists)
📄 cpu_id                       - CPU identifier (removed if exists)
📄 gpu_id                       - GPU identifier (removed if exists)
```

#### 📊 **Configuration Files Modified**
```
📄 User/globalStorage/storage.json - Main telemetry configuration (cleaned)
📄 config.json - Tool configuration file
📄 User/settings.json - Qoder settings (auto-update control)
```

**Removed Keys from storage.json (Cleanup Mode):**
```json
{
  "telemetry.machineId": "REMOVED",
  "telemetry.devDeviceId": "REMOVED",
  "telemetry.sqmId": "REMOVED", 
  "telemetry.sessionId": "REMOVED",
  "telemetry.installationId": "REMOVED",
  "telemetry.clientId": "REMOVED", 
  "telemetry.userId": "REMOVED",
  "telemetry.anonymousId": "REMOVED",
  "machineId": "REMOVED",
  "deviceId": "REMOVED",
  "installationId": "REMOVED",
  "hardwareId": "REMOVED",
  "platformId": "REMOVED",
  "system.platform": "REMOVED",
  "system.arch": "REMOVED", 
  "system.version": "REMOVED",
  "system.timezone": "REMOVED"
}
```

**Tool Configuration (config.json):**
```json
{
  "create_backups": false,
  "disable_auto_update": true
}
```

#### 🛡️ **Hardware Fingerprint Files (Removed)**
```
📄 hardware_detection.json      - Removed if exists
📄 device_capabilities.json     - Removed if exists
📄 system_features.json         - Removed if exists
📄 platform_detection.json      - Removed if exists
```

**Hardware Cache Directories Cleared:**
```
📁 GPUCache/                    - GPU processing cache (cleared)
📁 DawnGraphiteCache/           - Graphics rendering cache (cleared)
📁 DawnWebGPUCache/             - WebGPU cache (cleared)
📁 ShaderCache/                 - Shader compilation cache (cleared)
```

### Files and Directories Deleted

#### 🌐 **Network Identity Files (Critical)**
```
📄 Network Persistent State     - Network connection history and fingerprints
📄 TransportSecurity            - HSTS and security policies 
📄 Trust Tokens                 - Trust token database
📄 Trust Tokens-journal         - Trust token journal
📄 SharedStorage                - Shared storage database
📄 SharedStorage-wal            - Shared storage WAL file
```

#### 🔐 **Authentication & Identity Files**
```
📄 Preferences                  - User preferences (may contain fingerprints)
📄 Secure Preferences           - Encrypted preferences
📄 Local State                  - Chromium local state
📄 DeviceMetadata               - Device metadata
📄 HardwareInfo                 - Hardware information
📄 SystemInfo                   - System information
📄 Login Credentials            - Stored login data
📄 AutofillStrikeDatabase       - Autofill database
📄 AutofillStrikeDatabase-journal - Autofill journal
```

#### 🗂️ **Cache Directories Cleared**
```
📁 Cache/                       - General application cache
📁 blob_storage/                - Binary data storage
📁 Code Cache/                  - JavaScript code cache
📁 GPUCache/                    - GPU processing cache
📁 DawnGraphiteCache/           - Graphics rendering cache
📁 DawnWebGPUCache/             - WebGPU cache
📁 ShaderCache/                 - Shader compilation cache
📁 CachedData/                  - Cached application data
📁 CachedProfilesData/          - User profile cache
📁 CachedExtensions/            - Extension cache
📁 IndexedDB/                   - Database cache
📁 CacheStorage/                - Storage API cache
📁 WebSQL/                      - WebSQL database cache
📁 Dictionaries/                - Dictionary cache
```

#### 📱 **SharedClientCache Directory**
```
📄 SharedClientCache/.info      - Client connection info (DELETED)
📄 SharedClientCache/.lock      - Process lock file (DELETED)
📄 SharedClientCache/auth.json  - Authentication data (DELETED)  
📄 SharedClientCache/server.json - Server configuration (DELETED)
📁 SharedClientCache/cache/     - Client cache directory (DELETED)
```

### Files and Directories Preserved

#### 💬 **Data Always Preserved**
```
📁 User/workspaceStorage/*/chatSessions/ - Chat session files ✅
📁 User/workspaceStorage/*/chatEditingSessions/ - Chat editing sessions ✅
📁 User/History/                - Command history ✅
📄 User/settings.json          - User settings ✅ (auto-update may be modified)
📄 SharedClientCache/mcp.json   - MCP configuration ✅ (CRITICAL)
📄 machineid                    - Main machine ID file ✅ (managed separately)
```

#### ⚡ **Live Machine ID Change**
```
🔧 Memory Injection             - Direct process memory modification
💾 ID Persistence              - Save/load machine IDs from AppData/Roaming/Qoder/
🎯 Process Targeting            - Automatic Qoder process detection
⚠️ Administrator Required       - Elevated privileges for memory access
```

## 🔒 Safety Features

### Configuration Management System

The tool uses JSON-based configuration for runtime behavior:

#### Configuration Features:
- **Runtime Control**: `config.json` controls tool behavior without UI interaction
- **Auto-Update Management**: Automatically disables Qoder auto-update if configured
- **Backup Control**: Backups are disabled by default for faster operation
- **Persistent Settings**: Configuration survives tool restarts

#### Configuration Example:
```
📄 config.json
{
  "create_backups": false,
  "disable_auto_update": true
}
```

### Process and Operation Safety

- **🔍 Process Detection**: Automatically detects running Qoder processes
- **⚠️ Context-Aware Operations**: 
  - Cleanup mode: Prevents operations while Qoder is running
  - Live change mode: Requires Qoder to be running
- **🛡️ Cross-Platform**: Works on Windows, macOS, and Linux
- **📝 Clear Messaging**: Detailed status messages and error handling
- **🔧 Administrator Privileges**: Required for live machine ID changes

### Data Protection

- **💬 Conversation Preservation**: All chat history and editing sessions are preserved
- **🔧 Configuration Safety**: Critical MCP settings are never deleted
- **📊 Selective Cleanup**: Only detectable files are removed, functionality preserved
- **🎯 Smart Preservation**: Automatically preserves important configuration files
- **⚡ Live Modification**: Machine ID changes without file system impact

## 🚨 Troubleshooting

### Common Issues

#### 1. **"Qoder is running" Error (Cleanup Mode)**
```
Solution: Close Qoder completely before running cleanup
- Use Ctrl+Q (Cmd+Q on macOS) to quit Qoder
- Check Task Manager/Activity Monitor for remaining processes
```

#### 1a. **"Qoder is not running" Error (Change Machine ID Mode)**
```
Solution: Start Qoder before using machine ID change
- Launch Qoder application
- Wait for it to fully load
- Run the tool as administrator
```

#### 2. **"Directory not found" Error**  
```
Solution: Ensure Qoder has been run at least once
- Launch Qoder to create configuration directories
- Verify installation path is correct
```

#### 3. **Permission Denied Errors**
```bash
# Windows: Run as Administrator
# macOS/Linux: Check directory permissions
chmod -R u+rw ~/Library/Application\ Support/Qoder/
```

#### 4. **Python Dependencies Missing**
```bash
# Install all required packages
pip install -r requirements.txt

# Or install manually
pip install psutil rich pymem keyboard

# Verify installation  
python -c "import psutil, rich, pymem, keyboard; print('All dependencies available')"
```

#### 5. **Administrator Privileges Required (Machine ID Change)**
```
Solution: Run as administrator for machine ID changes
- Windows: Right-click PowerShell/CMD -> "Run as administrator"
- Run: python main.py
- Choose option 3 (Change Machine ID)
```

### Log Analysis

The tool provides detailed logging for troubleshooting:

**Cleanup Mode:**
```
[2025-08-31 14:30:52] 🚀 STARTING COMPREHENSIVE QODER CLEANUP
[2025-08-31 14:30:52] --- 🧹 Machine ID Cleanup ---
[2025-08-31 14:30:52]    ℹ️  Main machineid file preserved (managed by machine_id_changer)
[2025-08-31 14:30:52]    ✅ Removed: deviceid
[2025-08-31 14:30:52] --- 📊 Telemetry Data Cleanup ---  
[2025-08-31 14:30:53]    ✅ Removed 13 telemetry entries
[2025-08-31 14:30:53] 🎉 COMPREHENSIVE CLEANUP COMPLETED SUCCESSFULLY!
```

**Live Machine ID Change:**
```
[2025-08-31 14:35:15] ⚡ Starting machine ID change...
[2025-08-31 14:35:15] ✅ Qoder is running
[2025-08-31 14:35:16] Generated new machine ID: 87654321-4321-8765-2109-876543210fed
[2025-08-31 14:35:16] Found qoder.exe (pid 1234) -> freeze armed
[2025-08-31 14:35:16] Machine ID change started. Press Ctrl+C to exit.
```

### Status Indicators

- **✅ Success**: Operation completed successfully
- **⚠️ Warning**: Non-critical issue, operation continues
- **❌ Error**: Critical failure, operation may stop
- **ℹ️ Info**: Informational message
- **💾 Preserved**: File/directory was intentionally preserved

## ⚠️ Important Notes

### Before Using

1. **📚 Read Documentation**: Understand what each mode does before proceeding
2. **⚙️ Choose Mode Correctly**: 
   - **Cleanup**: Close Qoder completely before running
   - **Change Machine ID**: Qoder must be running and tool needs administrator privileges
3. **🔍 Test Environment**: Consider testing in a non-production environment first
4. **💾 Important Files**: The tool preserves MCP settings and conversations automatically

### After Cleanup

1. **🔄 Restart Qoder**: Launch Qoder to verify functionality after cleanup
2. **🌐 Use Fingerprint Browser**: Use fingerprint-protected browser for new registrations
3. **🔐 Re-login**: You may need to log in to Qoder again
4. **📊 Verify Operation**: Check that Qoder works normally with preserved settings

### After Live Machine ID Change

1. **⚡ Immediate Effect**: Machine ID change takes effect immediately while Qoder runs
2. **💾 ID Persistence**: New machine ID is saved for future use
3. **🔄 No Restart Required**: Changes apply without restarting Qoder
4. **📊 Verify in Memory**: Machine ID is actively maintained in Qoder's memory

### Data Safety

- **💬 Conversations**: All chat history is preserved by default
- **🔧 Settings**: User preferences and MCP configuration are maintained
- **📁 Workspaces**: All workspace data remains intact
- **🧹 Cleanup Only**: Only detectable files are removed, core functionality preserved
- **⚡ Live Changes**: Machine ID changes don't affect file system or user data

## 📄 License

This project is for educational and research purposes only. Please comply with relevant laws and software usage agreements.

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the detailed logs for error messages  
3. Create an issue with detailed information about your system and the problem

---

## 🎉 Getting Started

### One-Command Quick Start

```bash
# Install dependencies and run
pip install psutil rich pymem keyboard && python main.py
```

### In the menu:
1. Choose option **1** to check your current system status
2. Choose option **2** to cleanup detectable files (close Qoder first)
3. Choose option **3** to change machine ID live (Qoder must be running, requires admin)
4. Monitor the detailed progress logs
5. Continue using Qoder with cleaned/changed identity!

### Mode Selection Guide:
- **🔍 CHECK**: Always safe to run, shows current status
- **🧹 CLEANUP**: Use when Qoder is closed, removes detectable files
- **⚡ CHANGE MACHINE_ID**: Use when Qoder is running, requires administrator privileges

This tool provides comprehensive Qoder identity management, covering detection cleanup and live machine ID modification while maintaining complete data safety through smart preservation of critical files and settings.