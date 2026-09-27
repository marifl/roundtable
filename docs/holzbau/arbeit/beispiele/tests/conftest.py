"""Gemeinsame Test-Einstellungen: Beispielordner auf den Importpfad legen."""
import sys
from pathlib import Path

BEISPIELE = Path(__file__).resolve().parents[1]
if str(BEISPIELE) not in sys.path:
    sys.path.insert(0, str(BEISPIELE))
