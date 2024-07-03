import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._retailer_code = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer = None

    def handle_top_vendite(self, e):
        top_vendite = self._model.get_top_sales(self._anno, self._brand, self._retailer_code)
        self._view.txt_result.controls.clear()
        if len(top_vendite) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita con i filtri selezionati"))
        else:
            for vendita in top_vendite:
                self._view.txt_result.controls.append(ft.Text(vendita))
        self._view.update_page()

    def handle_analizza_vendite(self, e):
        statistiche_vendite = self._model.get_sales_stats(self._anno, self._brand, self._retailer_code)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Satistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {statistiche_vendite[0]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {statistiche_vendite[1]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero retailers coinvolti: {statistiche_vendite[2]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {statistiche_vendite[3]}"))
        self._view.update_page()

    def leggi_anni(self, e):
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value

    def populate_dd_anno(self):
        anni = self._model.get_anni()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def leggi_brand(self, e):
        if e.control.value == "None":
            self._brand = None
        else:
            self._brand = e.control.value

    def populate_dd_brand(self):
        brands = self._model.get_brands()
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand[0]))
        self._view.update_page()

    def leggi_retailer(self, e):
        if e.control.data is None:
            self._retailer_code = None
        else:
            self._retailer_code = e.control.data.retailer_code

    def populate_dd_retailer(self):
        retailers = self._model.get_retailers()
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(text=retailer.retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.leggi_retailer))
        self._view.update_page()



