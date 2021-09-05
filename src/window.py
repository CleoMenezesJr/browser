# window.py
#
# Copyright 2021 Cleo Menezes Jr.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, WebKit2


@Gtk.Template(resource_path='/org/gnome/browser/window.ui')
class BrowserWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'BrowserWindow'


    url_entry = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.web_view = WebKit2.WebView()
        self.web_view.load_uri('https://gnome.org')
        self.web_view.connect('notify::uri', self.url_changed)
        self.add(self.web_view)

        self.show_all()

    @Gtk.Template.Callback()
    def on_uri_entry_activated(self, entry):
        uri = entry.get_text()
        self.web_view.load_uri(uri)

    @Gtk.Template.Callback()
    def on_previous_button_clicked(self, button):
        self.web_view.go_back()

    @Gtk.Template.Callback()
    def on_next_button_clicked(self, button):
        self.web_view.go_forward()


    @Gtk.Template.Callback()
    def on_reload_button_clicked(self, button):
        self.web_view.reload()


    def url_changed(self, source, widget):
        url = self.web_view.get_uri()
        self.url_entry.set_text(url)
