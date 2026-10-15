import json
import base64
from pathlib import Path

out_dir = Path('Time Series/figures')
out_dir.mkdir(exist_ok=True, parents=True)
notebooks = [
    'Time Series/Time Series Analysis.ipynb',
    'Time Series/Time-series data analysis using LSTM .ipynb',
]
idx = 0
for nb_name in notebooks:
    path = Path(nb_name)
    nb = json.loads(path.read_text(encoding='utf-8'))
    for cell in nb.get('cells', []):
        for output in cell.get('outputs', []):
            png = output.get('data', {}).get('image/png')
            if png and idx < 8:
                filename = f'{path.stem}_{idx}.png'
                (out_dir / filename).write_bytes(base64.b64decode(png))
                idx += 1

print(f'Extracted {idx} images to {out_dir}')
