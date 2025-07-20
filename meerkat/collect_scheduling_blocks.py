#!/usr/bin/env python3
"""
Read meerkat_downloads.csv:
SBID,Target,StartUTC,URL
Create a subdirectory per input row and download the file(s) with wget -c.
"""
import csv, os, pathlib, requests, subprocess, re, textwrap
from time import time

base_dir = "MeerKAT_Data"

with open("meerKAT_links.csv") as f:
    reader = list(csv.DictReader(f))  # Convert to list to get length
    total = len(reader)

    for i, row in enumerate(reader, 1):
        folder_name = f"{row['Date']}_{row['Target']}_{row['Object']}_{row['Band']}".replace(" ", "_")
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        url = row['Download_URL']
        file_name = url.split('/')[-1]
        dest_path = os.path.join(folder_path, file_name)

        print(f"[{i}/{total}] Downloading: {row['Target']} ({row['SBID']})")
        print(f"   -> URL: {url}")
        print(f"   -> Saving to: {dest_path}")

        if not os.path.exists(dest_path):
            try:
                t0 = time()
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    with open(dest_path, "wb") as out:
                        for chunk in r.iter_content(chunk_size=8192):
                            out.write(chunk)
                print(f" Done in {int(time() - t0)} seconds.\n")
            except Exception as e:
                print(f" Error downloading: {e}\n")
        else:
            print(" Already exists — skipping.\n")

