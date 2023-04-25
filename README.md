# Dropbox Automations

![dropbox_automations](https://user-images.githubusercontent.com/37108394/234244745-53eea842-3003-4ba7-a32b-45e72af183cc.png)

`dropbox-automations` is a Python-based tool designed to streamline the process of working with shared data on Dropbox. It is particularly useful in scenarios where multiple users, such as medical professionals, are collaborating on shared data, such as medical imaging files.

With this tool, users can automate various operations, such as listing files in specified directories, downloading single or multiple files from one or more folders, and keeping track of new cases that have been uploaded. The primary goal is to eliminate the need to manually navigate the Dropbox website and enable seamless access to the data via a script.

## Features
- Authenticate with Dropbox using an access token
- List available files in a given directory
- Download individual files, multiple files, or files from multiple folders
- Automatically detect and download new files that have been uploaded
- Simplify data sharing and collaboration for medical imaging or other use cases

By using `dropbox-automations`, you can easily automate your Dropbox operations and streamline the process of accessing and managing shared data, thus improving efficiency and collaboration among team members.

## Packages
- Dropbox: ```pip install dropbox```
- PyYaml: ```pip install PyYAML```
- Shutil: ```pip install pytest-shutil```

## How Dropbox Automations works
```mermaid
sequenceDiagram
    actor User
    participant DropboxAutomations
    participant DropboxAPI
    participant LocalFileSystem
    autonumber

    Note over DropboxAutomations, LocalFileSystem: Initialization phase
    User ->> DropboxAutomations: Provide access token
    DropboxAutomations ->> DropboxAPI: Authenticate using access token

    Note over DropboxAutomations, LocalFileSystem: Listing phase
    User ->> DropboxAutomations: Request files in a specified directory
    DropboxAutomations ->> DropboxAPI: Retrieve files in the directory
    DropboxAPI -->> DropboxAutomations: Return file list
    DropboxAutomations -->> User: Display file list

    Note over DropboxAutomations, LocalFileSystem: Downloading phase
    User ->> DropboxAutomations: Specify files or folders to download
    DropboxAutomations ->> DropboxAPI: Download requested files
    DropboxAPI -->> DropboxAutomations: Return file content
    DropboxAutomations ->> LocalFileSystem: Save files to local system

    Note over DropboxAutomations, LocalFileSystem: Detecting new files phase
    loop Every X time
        DropboxAutomations ->> DropboxAPI: Check for new files in specified folders
        DropboxAPI -->> DropboxAutomations: Return new files list
        DropboxAutomations -->> User: Notify about new files
        User ->> DropboxAutomations: Download new files (optional)
    end


```
