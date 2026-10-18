# RaunakEduc animated GitHub profile

1. Create a public repository named exactly `RaunakEduc`. If it already exists, back up its README first.
2. Install Python 3.11+ and Git. In this directory run:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   python -m pip install -r scripts/requirements.txt
   python scripts/make_ascii_svg.py
   python scripts/make_info_card.py
   python scripts/fetch_contributions.py
   python scripts/render_heatmap_svg.py
   ```

3. Edit `scripts/profile.json` to add your role, current focus, stack, and a highlight, then rerun `python scripts/make_info_card.py`.
4. Review the README and push the folder contents to the `main` branch of `RaunakEduc/RaunakEduc`.
5. In Settings → Actions → General, allow workflow write access if needed. Run **Actions → Update profile art → Run workflow** once.

The ZIP includes the generated portrait SVG but excludes the original photo. To regenerate the portrait later, put your photo in this folder as `source-photo.jpg` first; `.gitignore` keeps it out of Git. The daily action refreshes the contribution graph.
