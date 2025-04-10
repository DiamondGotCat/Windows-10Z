#!/usr/bin/env python

from PySide6.QtWidgets import (
    QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFrame, QSizePolicy
)
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QSize


class SvgDisplayWidget(QWidget):
    def __init__(self, svg_path, max_width=300):
        super().__init__()
        self.renderer = QSvgRenderer(svg_path)
        self.max_width = max_width
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedSize(self.sizeHint())

    def sizeHint(self):
        original_size = self.renderer.defaultSize()
        scale = self.max_width / original_size.width()
        return QSize(self.max_width, int(original_size.height() * scale))

    def paintEvent(self, event):
        painter = QPainter(self)
        self.renderer.render(painter, self.rect())


class WinverWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Windows")
        self.setFixedSize(520, 440)

        self.setStyleSheet("background-color: #FFFFFF;")

        main_layout = QVBoxLayout(self)

        # --- ロゴ ---
        logo = SvgDisplayWidget("/etc/windows/winver/windows10_logo.svg", max_width=400)
        logo_layout = QHBoxLayout()
        logo_layout.addStretch()
        logo_layout.addWidget(logo)
        logo_layout.addStretch()
        main_layout.addLayout(logo_layout)

        # --- Divider ---
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(divider)

        # --- テキストブロック全体を中央に配置 ---
        text_block_layout = QHBoxLayout()
        text_block_layout.addStretch()

        content_text = (
            "<div style='text-align: left;'>"
            "Microsoft Windows<br>"
            "Version 1.0 (OS Build 129)<br>"
            "© 2019 Microsoft Corporation. All rights reserved.<br><br>"
            "The Windows 10Z Pro operating system and its user interface are protected by trademark and other pending or existing intellectual property rights in the United States and other countries/regions.<br><br>"
            "This product is licensed under the <a href='https://www.microsoft.com/en-us/useterms'>Microsoft Software Licence Terms</a> to:<br>"
            "<b>DiamondGotCat</b>"
            "</div>"
        )

        text_label = QLabel(content_text)
        text_label.setWordWrap(True)
        text_label.setOpenExternalLinks(True)
        text_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        text_label.setStyleSheet("font-size: 12px;")
        text_block_layout.addWidget(text_label)
        text_block_layout.addStretch()

        main_layout.addLayout(text_block_layout)

        # --- OKボタン ---
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        ok_button = QPushButton("OK")
        ok_button.setFixedWidth(80)
        ok_button.clicked.connect(self.close)
        button_layout.addWidget(ok_button)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = WinverWindow()
    window.show()
    sys.exit(app.exec())
