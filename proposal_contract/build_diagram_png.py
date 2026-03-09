#!/usr/bin/env python3
"""
Build architecture_diagram.png using matplotlib (no Cairo required).
Run from proposal_contract: python build_diagram_png.py
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# Dragonfruit colours from brief / brand
BG = "#FAFAFA"
SURFACE = "#FFFFFF"
TEXT = "#1a1a1a"
MUTED = "#64748B"
ACCENT = "#E85D75"
BORDER = "#E2E8F0"

fig, ax = plt.subplots(figsize=(11, 7.5), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 11)
ax.set_ylim(0, 7.5)
ax.axis("off")

def box(ax, x, y, w, h, label, sublabel=None, accent=False, fontsize=9):
    fc = ACCENT if accent else SURFACE
    ec = ACCENT if not accent else "white"
    lw = 2 if not accent else 0
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                       facecolor=fc, edgecolor=ec, linewidth=lw)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2 + (0.12 if sublabel else 0), label, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=TEXT if not accent else "white")
    if sublabel:
        ax.text(x + w/2, y + h/2 - 0.12, sublabel, ha="center", va="center", fontsize=7, color=MUTED if not accent else "white")

def layer_label(ax, y, text):
    ax.text(0.5, y, text, fontsize=10, fontweight="bold", color=MUTED, va="center")

# Title
ax.text(5.5, 7.2, "Dragonfruit Media — How we add AI to your pipeline", ha="center", fontsize=14, fontweight="bold", color=TEXT)
ax.text(5.5, 6.95, "Scale 4 → 7 clients per pod · Your tools stay. We add a layer that automates coordination.", ha="center", fontsize=9, color=MUTED)

# Layer 1: What you have today (where work comes from)
ax.add_patch(FancyBboxPatch((0.2, 5.5), 10.6, 1.0, boxstyle="round,pad=0.02", facecolor=SURFACE, edgecolor=BORDER))
ax.text(5.5, 6.32, "1. WHERE WORK COMES IN (today)", ha="center", fontsize=9, fontweight="bold", color=MUTED)
box(ax, 0.5, 5.55, 1.4, 0.38, "Slack", "messages, requests")
box(ax, 2.1, 5.55, 1.4, 0.38, "ClickUp", "tasks, status")
box(ax, 3.7, 5.55, 1.4, 0.38, "Frame.io", "review, comments")
box(ax, 5.3, 5.55, 1.4, 0.38, "Notion", "docs, SOPs")
box(ax, 6.9, 5.55, 1.4, 0.38, "Dropbox", "new footage")
box(ax, 8.5, 5.55, 2.0, 0.38, "Your team", "Producer, PC, CD, PPM")

# Arrow
ax.annotate("", xy=(5.5, 5.35), xytext=(5.5, 5.5), arrowprops=dict(arrowstyle="->", color=ACCENT, lw=2))

# Layer 2: What we add — AI layer (role-based)
ax.add_patch(FancyBboxPatch((0.2, 3.6), 10.6, 1.55, boxstyle="round,pad=0.02", facecolor=SURFACE, edgecolor=BORDER))
ax.text(5.5, 5.12, "2. WHAT WE ADD — AI that understands your roles (you still approve)", ha="center", fontsize=9, fontweight="bold", color=MUTED)
box(ax, 0.45, 3.65, 2.45, 1.35, "Producer Agent", "Creates tasks in ClickUp from plain language.\nYou confirm before anything is created.", accent=False)
ax.text(2.675, 3.82, "You approve: new tasks", fontsize=7, color=ACCENT, ha="center", fontweight="bold")
box(ax, 3.15, 3.65, 2.45, 1.35, "PC Agent", "Status updates, client messages, Slack.\nYou approve before sending to clients.", accent=False)
ax.text(4.375, 3.82, "You approve: client messages", fontsize=7, color=ACCENT, ha="center", fontweight="bold")
box(ax, 5.85, 3.65, 2.45, 1.35, "CD Agent", "Retention, competitor intel, packaging.\nAlerts you; you decide what to do.", accent=False)
box(ax, 8.55, 3.65, 2.2, 1.35, "PPM Agent", "QC reports, who’s free, assignees.\nYou confirm who gets the edit.", accent=False)
ax.text(9.65, 3.82, "You approve: assignments", fontsize=7, color=ACCENT, ha="center", fontweight="bold")

# Arrow
ax.annotate("", xy=(5.5, 3.45), xytext=(5.5, 3.6), arrowprops=dict(arrowstyle="->", color=ACCENT, lw=2))

# Layer 3: Connectors (the wiring)
ax.add_patch(FancyBboxPatch((0.2, 2.25), 10.6, 1.0, boxstyle="round,pad=0.02", facecolor=SURFACE, edgecolor=BORDER))
ax.text(5.5, 3.12, "3. THE WIRING (connectors we build)", ha="center", fontsize=9, fontweight="bold", color=MUTED)
ax.text(2.2, 2.6, "Talks to ClickUp", ha="center", fontsize=8, color=TEXT)
ax.text(4.0, 2.6, "Talks to Slack", ha="center", fontsize=8, color=TEXT)
ax.text(5.5, 2.6, "Talks to Notion", ha="center", fontsize=8, color=TEXT)
ax.text(7.0, 2.6, "Talks to Frame.io", ha="center", fontsize=8, color=TEXT)
ax.text(8.8, 2.6, "QC & assignment", ha="center", fontsize=8, color=TEXT)

# Arrow
ax.annotate("", xy=(5.5, 2.1), xytext=(5.5, 2.25), arrowprops=dict(arrowstyle="->", color=ACCENT, lw=2))

# Layer 4: Your existing systems (unchanged)
ax.add_patch(FancyBboxPatch((0.2, 0.35), 10.6, 1.55, boxstyle="round,pad=0.02", facecolor=SURFACE, edgecolor=BORDER))
ax.text(5.5, 1.87, "4. YOUR EXISTING SYSTEMS (we don’t replace these)", ha="center", fontsize=9, fontweight="bold", color=MUTED)
box(ax, 0.5, 0.4, 1.9, 1.35, "ClickUp", "Tasks, spaces, lists", accent=True)
box(ax, 2.6, 0.4, 1.9, 1.35, "Slack", "Channels, DMs", accent=True)
box(ax, 4.7, 0.4, 1.9, 1.35, "Notion", "Docs, knowledge", accent=True)
box(ax, 6.8, 0.4, 1.9, 1.35, "Frame.io", "Review, assets", accent=True)
box(ax, 8.9, 0.4, 1.8, 1.35, "Make / Zapier", "Your automations", accent=True)

# Footer
ax.text(5.5, 0.12, "Human-in-the-loop: you approve task creation, assignments, and client-facing messages. No rip-and-replace.", ha="center", fontsize=8, color=MUTED, style="italic")

plt.tight_layout()
plt.savefig("architecture_diagram.png", dpi=150, facecolor=BG, edgecolor="none", bbox_inches="tight")
print("Saved architecture_diagram.png")
plt.close()
