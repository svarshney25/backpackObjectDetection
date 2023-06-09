{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNtaljXv1MEEqCO5mWmCkVJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/svarshney25/backpackObjectDetection/blob/main/apushProject.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "28__CT43mvpf",
        "outputId": "bb8dd122-1d1a-4a84-d204-3a28ad0c23eb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.22.0-py2.py3-none-any.whl (8.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.9/8.9 MB\u001b[0m \u001b[31m56.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: altair<5,>=3.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Collecting blinker>=1.0.0 (from streamlit)\n",
            "  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.3)\n",
            "Collecting importlib-metadata>=1.4 (from streamlit)\n",
            "  Downloading importlib_metadata-6.6.0-py3-none-any.whl (22 kB)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.22.4)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (23.1)\n",
            "Requirement already satisfied: pandas<3,>=0.25 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.5.3)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.4.0)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Collecting pympler>=0.9 (from streamlit)\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.8/164.8 kB\u001b[0m \u001b[31m8.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.27.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.3.4)\n",
            "Requirement already satisfied: tenacity<9,>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.2.2)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.5.0)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.3)\n",
            "Collecting validators>=0.2 (from streamlit)\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting gitpython!=3.1.19 (from streamlit)\n",
            "  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m184.3/184.3 kB\u001b[0m \u001b[31m9.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pydeck>=0.1.dev5 (from streamlit)\n",
            "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m38.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.1)\n",
            "Collecting watchdog (from streamlit)\n",
            "  Downloading watchdog-3.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m3.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (3.1.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.12.0)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19->streamlit)\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m613.7 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=1.4->streamlit) (3.15.0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=0.25->streamlit) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil->streamlit) (1.16.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (3.4)\n",
            "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.14.0)\n",
            "Requirement already satisfied: pytz-deprecation-shim in /usr/local/lib/python3.10/dist-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit)\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<5,>=3.2.0->streamlit) (2.1.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (23.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (0.19.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/dist-packages (from pytz-deprecation-shim->tzlocal>=1.1->streamlit) (2023.3)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19579 sha256=fbafaadfe6e80c6a52fb2bc43199ff0d8cfda51f3a0373a2f59e456917288a17\n",
            "  Stored in directory: /root/.cache/pip/wheels/f2/ed/dd/d3a556ad245ef9dc570c6bcd2f22886d17b0b408dd3bbb9ac3\n",
            "Successfully built validators\n",
            "Installing collected packages: watchdog, validators, smmap, pympler, importlib-metadata, blinker, pydeck, gitdb, gitpython, streamlit\n",
            "Successfully installed blinker-1.6.2 gitdb-4.0.10 gitpython-3.1.31 importlib-metadata-6.6.0 pydeck-0.8.1b0 pympler-1.0.1 smmap-5.0.0 streamlit-1.22.0 validators-0.20.0 watchdog-3.0.0\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit_embedcode\n",
            "  Downloading streamlit_embedcode-0.1.2-py3-none-any.whl (3.5 kB)\n",
            "Requirement already satisfied: streamlit>=0.63 in /usr/local/lib/python3.10/dist-packages (from streamlit_embedcode) (1.22.0)\n",
            "Requirement already satisfied: altair<5,>=3.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (4.2.2)\n",
            "Requirement already satisfied: blinker>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (1.6.2)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (5.3.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (8.1.3)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (6.6.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (1.22.4)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (23.1)\n",
            "Requirement already satisfied: pandas<3,>=0.25 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (1.5.3)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (8.4.0)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (9.0.0)\n",
            "Requirement already satisfied: pympler>=0.9 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (1.0.1)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (2.8.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (2.27.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (13.3.4)\n",
            "Requirement already satisfied: tenacity<9,>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (8.2.2)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (4.5.0)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (4.3)\n",
            "Requirement already satisfied: validators>=0.2 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (0.20.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (3.1.31)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (0.8.1b0)\n",
            "Requirement already satisfied: tornado>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (6.3.1)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_embedcode) (3.0.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit>=0.63->streamlit_embedcode) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit>=0.63->streamlit_embedcode) (3.1.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit>=0.63->streamlit_embedcode) (4.3.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit>=0.63->streamlit_embedcode) (0.12.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19->streamlit>=0.63->streamlit_embedcode) (4.0.10)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=1.4->streamlit>=0.63->streamlit_embedcode) (3.15.0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=0.25->streamlit>=0.63->streamlit_embedcode) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil->streamlit>=0.63->streamlit_embedcode) (1.16.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_embedcode) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_embedcode) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_embedcode) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_embedcode) (3.4)\n",
            "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit>=0.63->streamlit_embedcode) (2.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit>=0.63->streamlit_embedcode) (2.14.0)\n",
            "Requirement already satisfied: pytz-deprecation-shim in /usr/local/lib/python3.10/dist-packages (from tzlocal>=1.1->streamlit>=0.63->streamlit_embedcode) (0.1.0.post0)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from validators>=0.2->streamlit>=0.63->streamlit_embedcode) (4.4.2)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit>=0.63->streamlit_embedcode) (5.0.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<5,>=3.2.0->streamlit>=0.63->streamlit_embedcode) (2.1.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit>=0.63->streamlit_embedcode) (23.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit>=0.63->streamlit_embedcode) (0.19.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit>=0.63->streamlit_embedcode) (0.1.2)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/dist-packages (from pytz-deprecation-shim->tzlocal>=1.1->streamlit>=0.63->streamlit_embedcode) (2023.3)\n",
            "Installing collected packages: streamlit_embedcode\n",
            "Successfully installed streamlit_embedcode-0.1.2\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import cv2\n",
        "from PIL import Image, ImageEnhance\n",
        "import numpy as np\n",
        "import os\n",
        "#import tensorflow as tf\n",
        "#import tensorflow_hub as hub\n",
        "!pip install streamlit_embedcode\n",
        "from streamlit_embedcode import github_gist\n",
        "import time ,sys\n",
        "import urllib.request\n",
        "import urllib\n",
        "import moviepy.editor as moviepy\n",
        "import cv2\n",
        "import numpy as np\n",
        "import time\n",
        "import sys"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "    new_title = '<p style=\"font-size: 42px;\">Welcome to my Object Detection App!</p>'\n",
        "    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)\n",
        "\n",
        "    read_me = st.markdown(\"\"\"\n",
        "    This project was built using Streamlit and OpenCV \n",
        "    to demonstrate YOLO Object detection in both videos(pre-recorded)\n",
        "    and images.\n",
        "    \n",
        "    \n",
        "    This YOLO object Detection project can detect 80 objects(i.e classes)\n",
        "    in either a video or image. The full list of the classes can be found \n",
        "    [here](https://github.com/KaranJagtiani/YOLO-Coco-Dataset-Custom-Classes-Extractor/blob/main/classes.txt)\"\"\"\n",
        "    )\n",
        "    st.sidebar.title(\"Select Activity\")\n",
        "    choice  = st.sidebar.selectbox(\"MODE\",(\"About\",\"Object Detection(Image)\",\"Object Detection(Video)\"))\n",
        "    #[\"Show Instruction\",\"Landmark identification\",\"Show the #source code\", \"About\"]\n",
        "    \n",
        "    if choice == \"Object Detection(Image)\":\n",
        "        #st.subheader(\"Object Detection\")\n",
        "        read_me_0.empty()\n",
        "        read_me.empty()\n",
        "        #st.title('Object Detection')\n",
        "        object_detection_image()\n",
        "    elif choice == \"Object Detection(Video)\":\n",
        "        read_me_0.empty()\n",
        "        read_me.empty()\n",
        "        #object_detection_video.has_beenCalled = False\n",
        "        object_detection_video()\n",
        "        #if object_detection_video.has_beenCalled:\n",
        "        try:\n",
        "\n",
        "            clip = moviepy.VideoFileClip('detected_video.mp4')\n",
        "            clip.write_videofile(\"myvideo.mp4\")\n",
        "            st_video = open('myvideo.mp4','rb')\n",
        "            video_bytes = st_video.read()\n",
        "            st.video(video_bytes)\n",
        "            st.write(\"Detected Video\") \n",
        "        except OSError:\n",
        "            ''\n",
        "\n",
        "    elif choice == \"About\":\n",
        "        print()\n",
        "        \n",
        "\n",
        "if __name__ == '__main__':\n",
        "\t\tmain()\t"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9X-AifdBm0BW",
        "outputId": "04f2de66-537d-4e30-ec7c-d24c4e36ca5f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def object_detection_image():\n",
        "    st.title('Object Detection for Images')\n",
        "    st.subheader(\"\"\"\n",
        "    This object detection project takes in an image and outputs the image with bounding boxes created around the objects in the image\n",
        "    \"\"\")\n",
        "    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])\n",
        "    if file!= None:\n",
        "        img1 = Image.open(file)\n",
        "        img2 = np.array(img1)\n",
        "\n",
        "        st.image(img1, caption = \"Uploaded Image\")\n",
        "        my_bar = st.progress(0)\n",
        "        confThreshold =st.slider('Confidence', 0, 100, 50)\n",
        "        nmsThreshold= st.slider('Threshold', 0, 100, 20)\n",
        "        #classNames = []\n",
        "        whT = 320\n",
        "        url = \"https://raw.githubusercontent.com/zhoroh/ObjectDetection/master/labels/coconames.txt\"\n",
        "        f = urllib.request.urlopen(url)\n",
        "        classNames = [line.decode('utf-8').strip() for  line in f]\n",
        "        #f = open(r'C:\\Users\\Olazaah\\Downloads\\stream\\labels\\coconames.txt','r')\n",
        "        #lines = f.readlines()\n",
        "        #classNames = [line.strip() for line in lines]\n",
        "        config_path = r'config_n_weights\\yolov3.cfg'\n",
        "        weights_path = r'config_n_weights\\yolov3.weights'\n",
        "        net = cv2.dnn.readNetFromDarknet(config_path, weights_path)\n",
        "        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)\n",
        "        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)\n",
        "\n",
        "        def findObjects(outputs,img):\n",
        "            hT, wT, cT = img2.shape\n",
        "            bbox = []\n",
        "            classIds = []\n",
        "            confs = []\n",
        "            for output in outputs:\n",
        "                for det in output:\n",
        "                    scores = det[5:]\n",
        "                    classId = np.argmax(scores)\n",
        "                    confidence = scores[classId]\n",
        "                    if confidence > (confThreshold/100):\n",
        "                        w,h = int(det[2]*wT) , int(det[3]*hT)\n",
        "                        x,y = int((det[0]*wT)-w/2) , int((det[1]*hT)-h/2)\n",
        "                        bbox.append([x,y,w,h])\n",
        "                        classIds.append(classId)\n",
        "                        confs.append(float(confidence))\n",
        "        \n",
        "            indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold/100, nmsThreshold/100)\n",
        "            obj_list=[]\n",
        "            confi_list =[]\n",
        "            #drawing rectangle around object\n",
        "            for i in indices:\n",
        "                i = i\n",
        "                box = bbox[i]\n",
        "                x, y, w, h = box[0], box[1], box[2], box[3]\n",
        "                # print(x,y,w,h)\n",
        "                cv2.rectangle(img2, (x, y), (x+w,y+h), (240, 54 , 230), 2)\n",
        "                #print(i,confs[i],classIds[i])\n",
        "                obj_list.append(classNames[classIds[i]].upper())\n",
        "                \n",
        "                confi_list.append(int(confs[i]*100))\n",
        "                cv2.putText(img2,f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',\n",
        "                          (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (240, 0, 240), 2)\n",
        "            df= pd.DataFrame(list(zip(obj_list,confi_list)),columns=['Object Name','Confidence'])\n",
        "            if st.checkbox(\"Show Object's list\" ):\n",
        "                \n",
        "                st.write(df)\n",
        "            if st.checkbox(\"Show Confidence bar chart\" ):\n",
        "                st.subheader('Bar chart for confidence levels')\n",
        "                \n",
        "                st.bar_chart(df[\"Confidence\"])\n",
        "           \n",
        "        blob = cv2.dnn.blobFromImage(img2, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)\n",
        "        net.setInput(blob)\n",
        "        layersNames = net.getLayerNames()\n",
        "        outputNames = [layersNames[i-1] for i in net.getUnconnectedOutLayers()]\n",
        "        outputs = net.forward(outputNames)\n",
        "        findObjects(outputs,img2)\n",
        "    \n",
        "        st.image(img2, caption='Proccesed Image.')\n",
        "        \n",
        "        cv2.waitKey(0)\n",
        "        \n",
        "        cv2.destroyAllWindows()\n",
        "        my_bar.progress(100)"
      ],
      "metadata": {
        "id": "4Hx2S5aNm6OC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def object_detection_video():\n",
        "    #object_detection_video.has_beenCalled = True\n",
        "    #pass\n",
        "    CONFIDENCE = 0.5\n",
        "    SCORE_THRESHOLD = 0.5\n",
        "    IOU_THRESHOLD = 0.5\n",
        "    config_path = r'config_n_weights\\yolov3.cfg'\n",
        "    weights_path = r'config_n_weights\\yolov3.weights'\n",
        "    font_scale = 1\n",
        "    thickness = 1\n",
        "    url = \"https://raw.githubusercontent.com/zhoroh/ObjectDetection/master/labels/coconames.txt\"\n",
        "    f = urllib.request.urlopen(url)\n",
        "    labels = [line.decode('utf-8').strip() for  line in f]\n",
        "    #f = open(r'C:\\Users\\Olazaah\\Downloads\\stream\\labels\\coconames.txt','r')\n",
        "    #lines = f.readlines()\n",
        "    #labels = [line.strip() for line in lines]\n",
        "    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype=\"uint8\")\n",
        "\n",
        "    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)\n",
        "\n",
        "    ln = net.getLayerNames()\n",
        "    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]\n",
        "    st.title(\"Object Detection for Videos\")\n",
        "    st.subheader(\"\"\"\n",
        "    This object detection project takes in a video and outputs the video with bounding boxes created around the objects in the video \n",
        "    \"\"\"\n",
        "    )\n",
        "    uploaded_video = st.file_uploader(\"Upload Video\", type = ['mp4','mpeg','mov'])\n",
        "    if uploaded_video != None:\n",
        "        \n",
        "        vid = uploaded_video.name\n",
        "        with open(vid, mode='wb') as f:\n",
        "            f.write(uploaded_video.read()) # save video to disk\n",
        "\n",
        "        st_video = open(vid,'rb')\n",
        "        video_bytes = st_video.read()\n",
        "        st.video(video_bytes)\n",
        "        st.write(\"Uploaded Video\")\n",
        "        #video_file = 'street.mp4'\n",
        "        cap = cv2.VideoCapture(vid)\n",
        "        _, image = cap.read()\n",
        "        h, w = image.shape[:2]\n",
        "        #out = cv2.VideoWriter(output_name, cv2.VideoWriter_fourcc#(*'avc3'), fps, insize)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "        fourcc = cv2.VideoWriter_fourcc(*'mpv4')\n",
        "        out = cv2.VideoWriter(\"detected_video.mp4\", fourcc, 20.0, (w, h))\n",
        "        count = 0\n",
        "        while True:\n",
        "            _, image = cap.read()\n",
        "            if _ != False:\n",
        "                h, w = image.shape[:2]\n",
        "                blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)\n",
        "                net.setInput(blob)\n",
        "                start = time.perf_counter()\n",
        "                layer_outputs = net.forward(ln)\n",
        "                time_took = time.perf_counter() - start\n",
        "                count +=1\n",
        "                print(f\"Time took: {count}\", time_took)\n",
        "                boxes, confidences, class_ids = [], [], []\n",
        "\n",
        "                # loop over each of the layer outputs\n",
        "                for output in layer_outputs:\n",
        "                    # loop over each of the object detections\n",
        "                    for detection in output:\n",
        "                        # extract the class id (label) and confidence (as a probability) of\n",
        "                        # the current object detection\n",
        "                        scores = detection[5:]\n",
        "                        class_id = np.argmax(scores)\n",
        "                        confidence = scores[class_id]\n",
        "                        # discard weak predictions by ensuring the detected\n",
        "                        # probability is greater than the minimum probability\n",
        "                        if confidence > CONFIDENCE:\n",
        "                            # scale the bounding box coordinates back relative to the\n",
        "                            # size of the image, keeping in mind that YOLO actually\n",
        "                            # returns the center (x, y)-coordinates of the bounding\n",
        "                            # box followed by the boxes' width and height\n",
        "                            box = detection[:4] * np.array([w, h, w, h])\n",
        "                            (centerX, centerY, width, height) = box.astype(\"int\")\n",
        "\n",
        "                            # use the center (x, y)-coordinates to derive the top and\n",
        "                            # and left corner of the bounding box\n",
        "                            x = int(centerX - (width / 2))\n",
        "                            y = int(centerY - (height / 2))\n",
        "\n",
        "                            # update our list of bounding box coordinates, confidences,\n",
        "                            # and class IDs\n",
        "                            boxes.append([x, y, int(width), int(height)])\n",
        "                            confidences.append(float(confidence))\n",
        "                            class_ids.append(class_id)\n",
        "\n",
        "                # perform the non maximum suppression given the scores defined before\n",
        "                idxs = cv2.dnn.NMSBoxes(boxes, confidences, SCORE_THRESHOLD, IOU_THRESHOLD)\n",
        "\n",
        "                font_scale = 0.6\n",
        "                thickness = 1\n",
        "\n",
        "                # ensure at least one detection exists\n",
        "                if len(idxs) > 0:\n",
        "                    # loop over the indexes we are keeping\n",
        "                    for i in idxs.flatten():\n",
        "                        # extract the bounding box coordinates\n",
        "                        x, y = boxes[i][0], boxes[i][1]\n",
        "                        w, h = boxes[i][2], boxes[i][3]\n",
        "                        # draw a bounding box rectangle and label on the image\n",
        "                        color = [int(c) for c in colors[class_ids[i]]]\n",
        "                        cv2.rectangle(image, (x, y), (x + w, y + h), color=color, thickness=thickness)\n",
        "                        text = f\"{labels[class_ids[i]]}: {confidences[i]:.2f}\"\n",
        "                        # calculate text width & height to draw the transparent boxes as background of the text\n",
        "                        (text_width, text_height) = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=font_scale, thickness=thickness)[0]\n",
        "                        text_offset_x = x\n",
        "                        text_offset_y = y - 5\n",
        "                        box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height))\n",
        "                        overlay = image.copy()\n",
        "                        cv2.rectangle(overlay, box_coords[0], box_coords[1], color=color, thickness=cv2.FILLED)\n",
        "                        # add opacity (transparency to the box)\n",
        "                        image = cv2.addWeighted(overlay, 0.6, image, 0.4, 0)\n",
        "                        # now put the text (label: confidence %)\n",
        "                        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,\n",
        "                            fontScale=font_scale, color=(0, 0, 0), thickness=thickness)\n",
        "\n",
        "                out.write(image)\n",
        "                cv2.imshow(\"image\", image)\n",
        "                \n",
        "                if ord(\"q\") == cv2.waitKey(1):\n",
        "                    break\n",
        "            else:\n",
        "                break\n",
        "\n",
        "\n",
        "        #return \"detected_video.mp4\"\n",
        "            \n",
        "        cap.release()\n",
        "        cv2.destroyAllWindows()"
      ],
      "metadata": {
        "id": "M0s3cCQLm8uL"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}