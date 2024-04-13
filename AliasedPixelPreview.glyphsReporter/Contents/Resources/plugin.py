from __future__ import annotations

import objc
from AppKit import NSBezierPath, NSColor
from GlyphsApp import Glyphs
from GlyphsApp.plugins import ReporterPlugin


class AliasedPixelPreview(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = Glyphs.localize(
            {
                "en": "Aliased Pixel Preview",
                "de": "Schwarzweiß-Pixelvorschau",
            }
        )

    @objc.python_method
    def background(self, layer):
        NSColor.controlTextColor().set()
        outline = layer.completeBezierPath
        # bounds = layer.bounds
        # <CoreFoundation.CGRect
        #     origin=<CoreFoundation.CGPoint x=100.0 y=-0.04>
        #     size=<CoreFoundation.CGSize width=1200.0 height=1000>>
        font = layer.font()
        step = font.upm // 18
        halfstep = step // 2
        for y in range(1200 // step, -400 // step, -1):
            for x in range(0, int(layer.width // step)):
                if outline.containsPoint_((x * step + halfstep, y * step + halfstep)):
                    NSBezierPath.fillRect_((x * step, y * step), (step, step))

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
