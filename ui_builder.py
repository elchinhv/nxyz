import flet as ft

def build_ui(parent):
    parent.controls.append(ft.Text("Hello from remote script!"))
    def on_click(e):
        e.page.snack_bar = ft.SnackBar(ft.Text("Remote button clicked"))
        e.page.snack_bar.open = True
        e.page.update()
    parent.controls.append(ft.ElevatedButton("Remote button", on_click=on_click))
    parent.update()
