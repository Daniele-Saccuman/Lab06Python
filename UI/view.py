import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_top_vendite = None
        self.btn_analizza_vendite = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.dd_anno = ft.Dropdown(label="Anno",
                                   width=400,
                                   hint_text="Selezionare un anno",
                                   options=[ft.dropdown.Option(key="None",
                                                               text="Nessun filtro")],
                                   on_change=self._controller.leggi_anni
                                   )
        self._controller.populate_dd_anno()

        self.dd_brand = ft.Dropdown(label="Brand",
                                   width=400,
                                   hint_text="Selezionare un brand",
                                   options=[ft.dropdown.Option(key="None",
                                                               text="Nessun filtro")],
                                   on_change=self._controller.leggi_brand
                                   )
        self._controller.populate_dd_brand()

        self.dd_retailer = ft.Dropdown(label="Retailer",
                                   width=400,
                                   hint_text="Selezionare un retailer",
                                   options=[ft.dropdown.Option(key="None",
                                                               text="Nessun filtro")],
                                   on_change=self._controller.leggi_retailer
                                   )
        self._controller.populate_dd_retailer()

        # button for the "hello" reply

        row1 = ft.Row([ft.Container(self.dd_anno, width=250),
                       ft.Container(self.dd_brand, width=250),
                       ft.Container(self.dd_retailer, width=400)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.btn_top_vendite = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handle_top_vendite)
        self.btn_analizza_vendite = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handle_analizza_vendite)

        row2 = ft.Row([ft.Container(self.btn_top_vendite, width=150),
                       ft.Container(self.btn_analizza_vendite, width=200)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller


    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
