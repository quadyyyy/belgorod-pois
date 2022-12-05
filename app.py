import sys
import io
import folium
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Белгородские достопримечательности')
        self.window_width, self.window_height = 1310, 670
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setStyleSheet('background-color: rgb(30, 30, 30); font-size: 35px')
        #self.setStyleSheet('font-size: 35px')
        self.setWindowFlags(self.windowFlags())


        layout = QVBoxLayout()
        self.setLayout(layout)


        # задаем карту / setting map
        coordinate = (50.595694, 36.587375) # задаем координаты стартовой точки
        mapboxtoken = 'API TOKEN HERE'
        mapboxurl = 'https://api.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}@2x.png?access_token=' + mapboxtoken

        # задаем саму карту
        m = folium.Map(
            location=coordinate,
            zoom_start=95,
            tiles=mapboxurl,
            attr='Mapbox'
        )

        tooltip = "Кликните для информации"

        # соборная площадь
        marker = folium.Marker(
            location=[50.595694, 36.587375],
            popup="<stong>Соборная площадь</stong>",
            tooltip=tooltip )

        marker.add_to(m)

        # музей курская битва
        marker = folium.Marker(
            location=[50.59139291354616, 36.587886771355244],
            popup='<stong>Музей-диорама\n "Курская Битва. Белгородское Направление"</stong>',
            tooltip=tooltip )

        marker.add_to(m)


        # памятник владмиру великому
        marker = folium.Marker(
            location=[50.580255103847705, 36.58382132424922],
            popup='<stong>Памятник князю Владимиру</stong>',
            tooltip=tooltip )

        marker.add_to(m)


        # Центральный парк имени В. И. Ленина
        marker = folium.Marker(
            location=[50.604452900159345, 36.58727489834365],
            popup='<stong>Центральный парк имени В. И. Ленина</stong>',
            tooltip=tooltip )

        marker.add_to(m)




        # сохранение инфы / saving data
        data = io.BytesIO()
        m.save(data, close_file=False)

        # вывод карты в qt / output map in qt app
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Закрываем приложение...')

