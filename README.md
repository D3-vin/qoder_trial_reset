# 🚀 Advanced Qoder Reset Tool

A comprehensive command-line tool for resetting Qoder application identity information with advanced anti-detection features and automatic backup system.

## 📢 Connect with Us

- **📢 Channel**: [https://t.me/D3_vin](https://t.me/D3_vin) - Latest updates and releases
- **💬 Chat**: [https://t.me/D3vin_chat](https://t.me/D3vin_chat) - Community support and discussions
- **📁 GitHub**: [https://github.com/D3-vin](https://github.com/D3-vin) - Source code and development

![Python](https://img.shields.io/badge/Python-3.6+-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-Educational%20Use-green)

**✨ Important Note: After resetting Qoder, please use a fingerprint-protected browser for registration to avoid detection of duplicate registration due to browser cache or fingerprints. The author has been using it for 2 days after reset.**

**Like Cursor and Augment, subsequent detection will become increasingly strict. No guarantee how long it will work - use it while you can.**

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
- **💻 Enhanced Machine ID Reset** - Generate new machine identifiers with backup files
- **📊 Advanced Telemetry Reset** - Reset comprehensive telemetry and device tracking data
- **🔥 Deep Identity Cleanup** - Remove network states, trust tokens, and local storage
- **🔐 Login Identity Cleanup** - Clear authentication tokens and session data
- **🛡️ Hardware Fingerprint Reset** - Generate fake hardware info (strongest anti-detection)
- **💬 Smart Conversation Management** - Preserve chat history and user settings
- **🧹 Advanced Cache Cleanup** - Clear application caches while protecting important data

### 🔒 Safety & Backup System
- **📋 Automatic Backups** - Timestamped backups before any file modification
- **🔍 Process Detection** - Prevents unsafe operations when Qoder is running  
- **💾 Metadata Preservation** - Uses `shutil.copy2()` for complete file metadata backup
- **🔄 Graceful Recovery** - Continues operation even if individual backup fails
- **📝 Comprehensive Logging** - Detailed operation logs with status indicators

### 🌍 Cross-Platform Support
- **Windows 10/11** - Full feature support (`%APPDATA%\Qoder`)
- **macOS 12+** - Complete compatibility (`~/Library/Application Support/Qoder`)
- **Linux** - Basic support with fallback paths

## 🖥️ System Requirements

- **Operating System**: Windows 10+, macOS 12+, or Linux
- **Python**: 3.6 or higher
- **Dependencies**: `psutil`
- **Disk Space**: At least 100MB free space
- **Permissions**: 
  - Windows: Read/write access to `%APPDATA%\Qoder`
  - macOS: Read/write access to `~/Library/Application Support/Qoder`
  - Linux: Read/write access to user application data directory

## 📦 Quick Installation

### Method 1: Direct Execution (Recommended)

```bash
# 1. Clone or download the repository
git clone <repository-url>
cd qoder-reset

# 2. Install dependencies
pip install psutil

# 3. Run the tool
python main.py
```

### Method 2: One-Command Setup

```bash
# Install and run in one go
pip install psutil && python main.py
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
🚀 ADVANCED QODER RESET TOOL 🚀
═══════════════════════════════════════════════════════════
🔍 1. CHECK - Comprehensive system status analysis
   • Process status • File integrity • Cache analysis

🔄 2. RESET - Complete advanced reset (All Features)
   ✅ Enhanced Machine ID & Telemetry Reset
   ✅ Deep Identity & Network State Cleanup  
   ✅ Advanced Cache & Storage Cleanup
   ✅ Hardware Fingerprint Reset & Fake Data Generation
   ✅ Login Identity & Authentication Cleanup
   ✅ Smart Conversation Management

🚪 3. EXIT - Close application
═══════════════════════════════════════════════════════════
💡 Tip: Run CHECK first to see what will be reset
```

### Quick Start Example

```bash
# 1. Run the tool
python main.py

# 2. Choose option 1 to check current status
1

# 3. Choose option 2 to perform complete reset  
2

# 4. Monitor the detailed progress logs
# 5. Choose option 3 to exit when done
3
```

## 🔧 Technical Details

### Architecture Overview

The tool implements a comprehensive 7-stage reset process:

1. **🔧 Enhanced Machine ID Reset** - Generate multiple machine identifiers
2. **📊 Advanced Telemetry Reset** - Reset 15+ telemetry identifiers  
3. **🧹 Advanced Cache Cleanup** - Clear 15+ cache directories
4. **🔥 Deep Identity Cleanup** - Remove network and authentication files
5. **🔐 Login Identity Cleanup** - Clear login credentials and session data
6. **🛡️ Hardware Fingerprint Reset** - Generate system-specific fake hardware
7. **💬 Smart Conversation Management** - Preserve important user data

### Core Technologies

- **Process Detection**: Cross-platform process monitoring with `psutil`
- **File Operations**: Safe file handling with `pathlib` and `shutil`
- **JSON Processing**: Configuration file manipulation with built-in `json` module
- **UUID Generation**: Cryptographically secure identifiers with `uuid.uuid4()`
- **Hash Generation**: SHA256 hashing for telemetry machine IDs
- **Platform Detection**: System-specific adaptations with `platform` module

## 📁 File Operations

### Files Created/Modified

#### 🔑 **Machine Identity Files**
```
📄 machineid                    - Primary machine UUID
📄 deviceid                     - Device identifier  
📄 hardware_uuid                - Hardware-specific UUID
📄 system_uuid                  - System identifier
📄 platform_id                  - Platform-specific ID
📄 installation_id              - Installation UUID
📄 cpu_id                       - CPU identifier (hardware fingerprint)
📄 gpu_id                       - GPU identifier (hardware fingerprint) 
📄 memory_id                    - Memory identifier (hardware fingerprint)
📄 board_serial                 - Motherboard serial (hardware fingerprint)
📄 bios_uuid                    - BIOS identifier (hardware fingerprint)
```

#### 📊 **Configuration Files Modified**
```
📄 User/globalStorage/storage.json - Main telemetry configuration
```

**Updated Keys in storage.json:**
```json
{
  "telemetry.machineId": "SHA256_HASH",
  "telemetry.devDeviceId": "UUID",
  "telemetry.sqmId": "UUID", 
  "telemetry.sessionId": "UUID",
  "telemetry.installationId": "UUID",
  "telemetry.clientId": "UUID", 
  "telemetry.userId": "UUID",
  "telemetry.anonymousId": "UUID",
  "machineId": "SHA256_HASH",
  "deviceId": "UUID",
  "installationId": "UUID",
  "hardwareId": "UUID",
  "platformId": "UUID",
  "system.platform": "darwin/win32/linux",
  "system.arch": "x64/arm64", 
  "system.version": "SYSTEM_VERSION",
  "system.timezone": "RANDOM_TIMEZONE"
}
```

#### 🛡️ **Fake Hardware Files Generated**
```
📄 hardware_detection.json      - Fake hardware detection data
📄 device_capabilities.json     - Fake device capabilities
📄 system_features.json         - Fake system features
📄 platform_detection.json      - Fake platform detection
```

**Example Fake Hardware (macOS):**
```json
{
  "cpu": {
    "name": "Apple M4 Pro",
    "cores": 12,
    "frequency": "3.2GHz"
  },
  "gpu": {
    "name": "Apple M4 Pro GPU",
    "memory": "24GB"
  },
  "memory": {
    "total": "32GB", 
    "type": "LPDDR5"
  },
  "system": {
    "platform": "darwin",
    "version": "14.2.1",
    "arch": "arm64"
  }
}
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

#### 💬 **Conversation Data (Always Preserved)**
```
📁 User/workspaceStorage/*/chatSessions/ - Chat session files ✅
📁 User/workspaceStorage/*/chatEditingSessions/ - Chat editing sessions ✅
📁 User/History/                - Command history ✅
📄 User/settings.json          - User settings ✅
```

#### 🔧 **Important Configuration (Always Preserved)**
```
📄 SharedClientCache/mcp.json   - MCP configuration ✅ (CRITICAL)
```

## 🔒 Safety Features

### Automatic Backup System

The tool creates comprehensive backups before any file modification:

#### Backup Features:
- **Timestamped Format**: `filename_YYYYMMDD_HHMMSS.extension`
- **Organized Location**: `[original_directory]/backup/`
- **Metadata Preservation**: Uses `shutil.copy2()` to preserve file permissions and timestamps
- **Failure Resilience**: Continues operation even if individual backups fail
- **Complete Recovery**: All original files can be restored from backups

#### Backup Example:
```
📁 Qoder/backup/
├── 📄 machineid_20250826_143052
├── 📄 storage_20250826_143052.json
└── 📄 Preferences_20250826_143053
```

### Process Safety

- **🔍 Process Detection**: Automatically detects running Qoder processes
- **⚠️ Safety Warnings**: Prevents operations while Qoder is running  
- **🛡️ Cross-Platform**: Works on Windows, macOS, and Linux
- **📝 Clear Messaging**: Detailed status messages and error handling

### Data Protection

- **💬 Conversation Preservation**: All chat history and editing sessions are preserved
- **🔧 Configuration Safety**: Critical MCP settings are never deleted
- **📊 Selective Updates**: Only identity-related keys in storage.json are modified
- **🔄 Rollback Capability**: Complete backup system enables full recovery

## 🚨 Troubleshooting

### Common Issues

#### 1. **"Qoder is running" Error**
```
Solution: Close Qoder completely before running the reset tool
- Use Ctrl+Q (Cmd+Q on macOS) to quit Qoder
- Check Task Manager/Activity Monitor for remaining processes
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
# Install required packages
pip install psutil

# Verify installation  
python -c "import psutil; print('psutil available')"
```

### Log Analysis

The tool provides detailed logging for troubleshooting:

```
[2025-01-26 14:30:52] 🚀 STARTING COMPREHENSIVE QODER RESET
[2025-01-26 14:30:52] --- 🔧 Resetting Machine ID (Enhanced) ---
[2025-01-26 14:30:52]    ✅ Backup created: /path/to/backup/machineid_20250126_143052
[2025-01-26 14:30:52]    ✅ Main machine ID reset: 12345678-1234-5678-9012-123456789abc
[2025-01-26 14:30:52]    ✅ Created: deviceid
[2025-01-26 14:30:52] --- 📊 Resetting Telemetry Data (Enhanced) ---  
[2025-01-26 14:30:53]    ✅ Enhanced telemetry reset completed
[2025-01-26 14:30:53]    📊 Updated 13 telemetry IDs
[2025-01-26 14:30:53] 🎉 COMPREHENSIVE RESET COMPLETED SUCCESSFULLY!
```

### Status Indicators

- **✅ Success**: Operation completed successfully
- **⚠️ Warning**: Non-critical issue, operation continues
- **❌ Error**: Critical failure, operation may stop
- **ℹ️ Info**: Informational message
- **💾 Preserved**: File/directory was intentionally preserved

## ⚠️ Important Notes

### Before Using

1. **📋 Create Backup**: Although the tool creates automatic backups, consider manual backup of important data
2. **🚪 Close Qoder**: Ensure Qoder is completely closed before running any reset operations  
3. **🔍 Test Environment**: Consider testing in a non-production environment first
4. **📚 Read Documentation**: Understand what files will be modified before proceeding

### After Reset

1. **🔄 Restart System**: Recommended after hardware fingerprint reset
2. **🌐 Use Fingerprint Browser**: Use fingerprint-protected browser for new registrations
3. **🔐 Re-login**: You will need to log in to Qoder again
4. **📊 Verify Changes**: Check that new machine IDs have been generated

### Data Safety

- **💬 Conversations**: All chat history is preserved by default
- **🔧 Settings**: User preferences and MCP configuration are maintained
- **📁 Workspaces**: All workspace data remains intact
- **🔑 Identity Only**: Only tracking and identity data is reset

## 📝 Version History

### v2.0.0 - Advanced Anti-Detection (Current)
- ⚡ **Complete 7-stage reset process** with all advanced features
- 🛡️ **Hardware fingerprint reset** with system-specific fake hardware generation
- 🔐 **Login identity cleanup** with selective authentication data removal
- 💾 **Enhanced backup system** with timestamped backups and metadata preservation
- 📊 **Advanced telemetry reset** with 15+ identifier updates
- 🧹 **Comprehensive cache cleanup** covering 15+ cache directories
- 💬 **Smart conversation management** with automatic data preservation
- 🌍 **Cross-platform support** for Windows, macOS, and Linux

### v1.x.x - Basic Versions
- Basic machine ID and telemetry reset
- Simple file operations
- Limited backup functionality

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
pip install psutil && python main.py
```

### In the menu:
1. Choose option **1** to check your current system status
2. Choose option **2** to perform the complete advanced reset
3. Monitor the detailed progress logs
4. Restart Qoder and enjoy your new identity!


This tool provides the most comprehensive Qoder identity reset available, covering all known detection vectors while maintaining complete data safety through automatic backups and selective preservation.