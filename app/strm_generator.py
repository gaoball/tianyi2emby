import os

def generate_strm(links):
    os.makedirs("strm_files", exist_ok=True)
    with open("app/data/links.txt", "a", encoding="utf-8") as f:
        for link in links:
            f.write(link.strip() + "\n")

    for i, link in enumerate(links):
        fake_file_id = f"file_{i}"
        with open(f"strm_files/video_{i}.strm", "w", encoding="utf-8") as sf:
            sf.write(f"http://localhost:8060/user/cloud_file?share_id={link.strip().split('/')[-1]}&file_id={fake_file_id}")