# Dropbox Automations

[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/channel/UCdYyILlPlehK4fKS5DiuMXQ) [![Blog](https://img.shields.io/badge/Blog-FFC800.svg?style=for-the-badge&logo=<badge>&logoColor=white)](https://pycad.co/dropbox-automations/) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)  [![Demo](https://img.shields.io/badge/Demo-0066ff.svg?style=for-the-badge&logo=<badge>&logoColor=<logo-color>)](https://github.com/amine0110/dropbox-automations/blob/main/demo.ipynb) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/pycad_/) [![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/pycadd/)

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

## Releases
| Release Version | Description | Available |
| --- | --- | --- |
| 1.0.0 | Automation: download one or multiple files from one or multiple folders with a fully automated process while also checking the new available data to be downloaded | 04/25/2023 |
| 2.0.0 | checkGPT: finding the corresponding segmentation for each volume (in case the annotators didn't spell well the name of the file) | Soon |

## 📩 Newsletter
Stay up-to-date on the latest in computer vision and medical imaging! Subscribe to my newsletter now for insights and analysis on the cutting-edge developments in this exciting field.

https://pycad.co/join-us/

## 🏫 Courses

| Title | Tags | Link |
| --- | --- | --- |
| How to Work With Dicom Using Python | `Dicom` `Medical Imaging` `Python` | [Udemy](https://www.udemy.com/course/how-to-work-with-dicom-using-python/?referralCode=ECBFF2BA3DED3608BE91) |
| How to Improve Medical Image Classification Results | `Medical Imaging` `Image Classification` `Python` | [YouTube](https://youtu.be/IXJMNGiBWy4) | 
| Automatic Liver Segmentation Using PyTorch and Monai | `Medical Imaging` `Image Segmentation` `Python` | [YouTube](https://youtu.be/AU4KlXKKnac) |
| Learn Tkinter from Scratch to Create Desktop Applications | `Python` `Tkinter` `GUI` | [YouTube](https://youtu.be/Fv82RX4cWW4) |
| Learn C++ for Beginners | `C++` `Basics` | [YouTube](https://youtu.be/94T4RQiD4Lo) |

Student's [Testimonials](https://pycad.co/testimonials/).
