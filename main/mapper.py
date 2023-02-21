"""Puts all films location on map as well as start point"""


from typing import List
import folium


def mapper(loc_lst: List[tuple], start_point, film_year: int) -> None:
    """Puts all point on map and saves it in the html file"""
    html = """<h4>Film name: {}</h4>
    Year: {},<br>
    Film address: {}
    """
    map_films = folium.Map(tiles = "Stamen Terrain", location=list(start_point), zoom_start=4)
    map_films.add_child(folium.Marker(location=list(start_point),
                        popup="Your location",
                        icon=folium.Icon(color = "red")))
    layer_top = folium.FeatureGroup(name="Top 10 Films map")
    for name, chords, address in loc_lst[:10]:
        iframe = folium.IFrame(html=html.format(name, film_year, address),
                        width=300,
                        height=100)
        layer_top.add_child(folium.Marker(location=[chords[0][0], chords[0][1]],
                popup=folium.Popup(iframe),
                icon=folium.Icon(color = "green")))
    layer_all = folium.FeatureGroup(name="All Films map")
    for name, chords, address in loc_lst:
        iframe = folium.IFrame(html=html.format(name, film_year, address),
                        width=300,
                        height=100)
        layer_all.add_child(folium.Marker(location=[chords[0][0], chords[0][1]],
                popup=folium.Popup(iframe),
                icon=folium.Icon(color = "orange")))
    map_films.add_child(layer_top)
    map_films.add_child(layer_all)
    map_films.add_child(folium.LayerControl())
    map_films.save("film_map.html")
