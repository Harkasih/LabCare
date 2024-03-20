# Print results
for c in det[:, 5].unique():
    n = (det[:, 5] == c).sum()  # detections per class
    if names[int(c)] == "apron":
        s += f"{n} jas lab{'s' * (n > 1)}, "  # add to string
    else:
        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

# Write results
for *xyxy, conf, cls in reversed(det):
    c = int(cls)  # integer class
    if names[c] == "apron":
        label = "jas lab"
    else:
        label = names[c] if hide_conf else f"{names[c]}"
    confidence = float(conf)
    confidence_str = f"{confidence:.2f}"

    if save_csv:
        write_to_csv(p.name, label, confidence_str)

    if save_txt:  # Write to file
        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
        if label == "jas lab":
            label = "4"  # Ganti indeks kelas "apron" dengan indeks kelas "jas lab" dalam file teks
        line = (label, *xywh, conf) if save_conf else (label, *xywh)  # label format
        with open(f"{txt_path}.txt", "a") as f:
            f.write(("%g " * len(line)).rstrip() % line + "\n")