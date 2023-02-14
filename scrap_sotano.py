import requests
from bs4 import BeautifulSoup
import csv
#1.- HACEMOS NUESTRO MARKUP DONDE VENDRA LA URL Y CONVERTIRLA EN .txt


labels=['Titulo','Autor','Precio'] #nuestras cabecera del excel.


def scrap_pg():
	Librero=[] #lista donde se anade el diccionario
	book_arr=[]
	markup=requests.get(f'https://www.elsotano.com/losmasvendidos').text
	soup=BeautifulSoup(markup,'html.parser')

	each_book= soup.find_all("div",class_="item")
	#print(each_book)
	for one_book in each_book:
		Dict_book={}  #guarda como clave : titulo, autor y precio.
		titulo= one_book.h3.find("a")["title"].title().strip() #extraemos unicamente el titulo dentro de la etiqueta  a
		t=""
		t=t+titulo #se concatenan cada titulo
		Dict_book['Titulo']=titulo #se agrega como valor cada titulo de mi diccionario 
		t="" #limpiamos la variable

		autor=one_book.find("span",class_="so-bookwriter").get_text().title().strip() #busca el autor
		a=""
		a=a+autor
		#print(type(a))
		Dict_book['Autor']=a
		a=""
		
		precio=one_book.select_one("ins").get_text().strip().replace("$","") #seleccionamos el precio final .strip() elimina espacios al inicio y final
		p=""
		p=p+precio
		#print(type(p))
		Dict_book['Precio']=p
		#print(precio)

		Librero.append(Dict_book) #lo agregamos a una lista.
		#print(Dict_book)
	try:
		with open('LibreriaSotano.csv','w') as f1:
			writer = csv.DictWriter(f1,fieldnames=labels)
			writer.writeheader()
			for elem in Librero: #recorremos cada elemento de nuestra lista donde se guarda el diccionario
				writer.writerow(elem)
	except IOError:
		print("I/O error")


if __name__ == "__main__": 
	scrap_pg() #llamamos a nuestra funcion


#15/01/2023
#creado  por luis juarez :D. 
#pagina que scrapiamos:  https://www.elsotano.com/novedades-editoriales