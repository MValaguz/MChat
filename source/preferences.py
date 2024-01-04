# -*- coding: utf-8 -*-

"""
 Creato da.....: Marco Valaguzza
 Piattaforma...: Python3.11 con libreria pyqt5
 Data..........: 29/11/2023
 Descrizione...: Gestione delle preferenze di MChat
 
 Note..........: Il layout è stato creato utilizzando qtdesigner e il file preferences.py è ricavato partendo da preferences_ui.ui 

 Note..........: Questo programma ha due funzioni. La prima di gestire a video le preferenze e la seconda di restituire una classe
                 che contiene le preferenze (preferences_class)
"""

#Librerie sistema
import sys
import os
import json
#Amplifico la pathname dell'applicazione in modo veda il contenuto della directory qtdesigner dove sono contenuti i layout
sys.path.append('qtdesigner')
#Librerie grafiche
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#Definizioni interfaccia
from preferences_ui import Ui_preferences_window
#Librerie aggiuntive interne
from utilita import message_info, message_question_yes_no

class preferences_class():
    """
        Classe che riporta tutte le preferenze
    """
    def __init__(self, p_nome_file_preferences):
        """
           Lettura del file delle preferenze e caricamento nella classe
        """
        # Se esiste il file delle preferenze...le carico nell'oggetto
        if os.path.isfile(p_nome_file_preferences):
            v_json = json.load(open(p_nome_file_preferences, 'r'))
            # posizione finestre        
            if v_json['remember_window_pos']==1:
                self.remember_window_pos = True
            else:
                self.remember_window_pos = False
            # font
            self.font_editor = v_json['font_editor']            
            # splash screen
            if v_json['splash'] == 1:
                self.splash = True
            else:
                self.splash = False
            # server
            self.elenco_server = v_json['server']
            # users
            self.elenco_user = v_json['users']
        # imposto valori di default senza presenza dello specifico file
        else:
            self.remember_window_pos = True            
            self.font_editor = 'MS Shell Dlg 2, 8'            
            self.splash = True
            # elenco server è composto da Titolo, TNS e Colore
            self.elenco_server = [('SERVER ONE','1250','#ffffff'),
                                  ('SERVER TWO','1300','#dfffff')]
            # elenco users è composto da Titolo, User, Password
            self.elenco_user = [('PC-MVALAGUZ','Vala','10.0.47.9'),
                                ('pc-aberlend','..','10.0.47.1'),
                                ('PC-MARIANNM','Mary','10.0.47.2'),                                
                                ('PC-TRAINIM','Marco','10.0.47.17')]
            # creo la dir dove andranno le preferenze              
            if not os.path.isdir('C:\\MChat'):
                os.makedirs('C:\\MChat')
       
class win_preferences_class(QMainWindow, Ui_preferences_window):
    """
        Gestione delle preferenze di MSql
    """                
    def __init__(self, p_nome_file_preferences):
        super(win_preferences_class, self).__init__()        
        self.setupUi(self)

        self.nome_file_preferences = p_nome_file_preferences

        # creo l'oggetto preferenze che automaticamente carica il file o le preferenze di default
        self.preferences = preferences_class(self.nome_file_preferences)        
        # le preferenze caricate vengono riportate a video
        self.e_remember_window_pos.setChecked(self.preferences.remember_window_pos)        
        self.e_default_font_editor.setText(self.preferences.font_editor)
        self.e_default_splash.setChecked(self.preferences.splash)           

        # preparo elenco server        
        self.o_server.setColumnCount(4)
        self.o_server.setHorizontalHeaderLabels(['Server title','ip Port','Color',''])           
        v_rig = 1                
        for record in self.preferences.elenco_server:                                    
            self.o_server.setRowCount(v_rig) 
            self.o_server.setItem(v_rig-1,0,QTableWidgetItem(record[0]))       
            self.o_server.setItem(v_rig-1,1,QTableWidgetItem(record[1]))                               
            self.o_server.setItem(v_rig-1,2,QTableWidgetItem(record[2]))                                           
            # come quarta colonna metto il pulsante per la scelta del colore
            v_color_button = QPushButton()            
            v_icon = QIcon()
            v_icon.addPixmap(QPixmap(":/icons/icons/color.gif"), QIcon.Normal, QIcon.Off)
            v_color_button.setIcon(v_icon)
            v_color_button.clicked.connect(self.slot_set_color_server)

            self.o_server.setCellWidget(v_rig-1,3,v_color_button)                               
            v_rig += 1
        self.o_server.resizeColumnsToContents()

        # preparo elenco user        
        self.o_users.setColumnCount(3)
        self.o_users.setHorizontalHeaderLabels(['PC-NAME','Title name','IP'])   
        v_rig = 1                
        for record in self.preferences.elenco_user:                                    
            self.o_users.setRowCount(v_rig) 
            self.o_users.setItem(v_rig-1,0,QTableWidgetItem(record[0]))       
            self.o_users.setItem(v_rig-1,1,QTableWidgetItem(record[1]))                               
            self.o_users.setItem(v_rig-1,2,QTableWidgetItem(record[2]))                               
            v_rig += 1
        self.o_users.resizeColumnsToContents()

    def slot_set_color_server(self):
        """
           Gestione della scelta dei colori sull'elenco dei server
        """
        # ottengo un oggetto index-qt della riga selezionata
        index = self.o_server.currentIndex()           
        # prendo la cella che contiene il colore in modo da aprire la selezione partendo dal colore corrente
        v_color_corrente = self.o_server.item( index.row(), 2).text()                        
        # apro la dialog color
        color = QColorDialog.getColor(QColor(v_color_corrente))                
        # imposto il colore
        self.o_server.setItem( index.row(), 2, QTableWidgetItem(color.name()) )            
    
    def slot_b_restore(self):
        """
           Ripristina tutte preferenze di default
        """
        if message_question_yes_no('Do you want to restore default preferences?') == 'Yes':
            # cancello il file delle preferenze
            if os.path.isfile(self.nome_file_preferences):
                os.remove(self.nome_file_preferences)

            # emetto messaggio di fine
            message_info('Preferences restored! Restart MSql to see the changes ;-)')
            # esco dal programma delle preferenze
            self.close()
    
    def slot_b_default_font_editor(self):
        """
           Scelta del font
        """
        # apro la dialog di scelta del font partendo da quello eventualmente già settato
        v_split = self.e_default_font_editor.text().split(',')
        v_font_pref = QFont(str(v_split[0]),int(v_split[1]))

        font, ok = QFontDialog.getFont(v_font_pref)
        if ok:
            v_text = font.family() + ', '+ str(font.pointSize())            
            if font.bold():
                v_text += ', BOLD'
            self.e_default_font_editor.setText(v_text)            

    def slot_b_server_add(self):
        """
           Crea una riga vuota dove poter inserire informazioni connessioni al server
        """
        self.o_server.setRowCount(self.o_server.rowCount()+1)

    def slot_b_server_remove(self):
        """
           Toglie la riga selezionata, da elenco server
        """
        self.o_server.removeRow(self.o_server.currentRow())

    def slot_b_user_add(self):
        """
           Crea una riga vuota dove poter inserire informazioni utente di connessione al server
        """
        self.o_users.setRowCount(self.o_users.rowCount()+1)

    def slot_b_user_remove(self):
        """
           Toglie la riga selezionata, da elenco user
        """
        self.o_users.removeRow(self.o_users.currentRow())

    def slot_b_save(self):
        """
           Salvataggio
        """	
        # il default per ricordare posizione della window
        if self.e_remember_window_pos.isChecked():
            v_remember_window_pos = 1
        else:
            v_remember_window_pos = 0
        
        # splash screen
        if self.e_default_splash.isChecked():
            v_splash = 1
        else:
            v_splash = 0
            
        # elenco dei server
        v_server = []
        for i in range(0,self.o_server.rowCount()):
            v_server.append( ( self.o_server.item(i,0).text(), self.o_server.item(i,1).text(), self.o_server.item(i,2).text() ) )            

        # elenco dei users
        v_users = []
        for i in range(0,self.o_users.rowCount()):
            v_users.append( ( self.o_users.item(i,0).text(), self.o_users.item(i,1).text() , self.o_users.item(i,2).text()) )            
	
		# scrivo nel file un elemento json contenente le informazioni inseriti dell'utente
        v_json ={'remember_window_pos': v_remember_window_pos,                 
		         'font_editor' :self.e_default_font_editor.text(),
                 'splash' : v_splash,                 
                 'server': v_server,
                 'users': v_users
                }

		# scrittura nel file dell'oggetto json
        with open(self.nome_file_preferences, 'w') as outfile:json.dump(v_json, outfile)
        
        message_info('Preferences saved! Restart MChat to see the changes ;-)')

# ----------------------------------------
# TEST APPLICAZIONE
# ----------------------------------------
if __name__ == "__main__":    
    app = QApplication([])
    application = win_preferences_class('C:\\MChat\\MChat.ini')
    application.show()
    sys.exit(app.exec())        