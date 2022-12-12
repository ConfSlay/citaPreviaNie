from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


import random
import time
import datetime

import smtplib
import ssl
from email.message import EmailMessage



browser  = webdriver.Chrome(ChromeDriverManager().install())


# =========== CONFIG VARIABLES ===========

city = "Valencia"
office = "CNP-COMISARIA DE BAILEN, Bailen, 9"
document = "POLICIA-CERTIFICADO DE REGISTRO DE CIUDADANO DE LA U.E"
document_value = "4038"
passport = "160575M00860"
full_name = "RICHARD PERRET"
# Define email sender and receiver
email_receiver = 'perretrichard1996@gmail.com'


# ========== CYBER WAR ==========
request_rejected_message = "The requested URL was rejected. Please consult with your administrator."




browser.implicitly_wait(10) #will automatically wait 10 sec if he doesnt find any element

# ================ SERVICE =============
# Open the Website
browser.get('https://icp.administracionelectronica.gob.es/icpplus/index')

# ------------- Page 1 --------------------------
assert request_rejected_message not in browser.page_source, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " " + request_rejected_message
time.sleep(random.randint(8,25))

# Select Provincia
select = Select(browser.find_element(By.NAME, 'form'))
select.select_by_visible_text(city)

time.sleep(random.randint(3,10))

# Click submit
element = browser.find_element(By.ID, 'btnAceptar')
browser.execute_script("arguments[0].click();", element)

# ------------- Page 2 --------------------------
assert request_rejected_message not in browser.page_source, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " " + request_rejected_message
time.sleep(random.randint(8,25))

# Select Provincia
select = Select(browser.find_element(By.ID, "sede"))
select.select_by_visible_text(office)

time.sleep(random.randint(3,10))

# Select document
select = Select(browser.find_element(By.ID, "tramiteGrupo[0]"))
select.select_by_value(document_value)

time.sleep(random.randint(3,10))

# Click submit
element = browser.find_element(By.ID, 'btnAceptar')
browser.execute_script("arguments[0].click();", element)

# ------------- Page 3 --------------------------
assert request_rejected_message not in browser.page_source, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " " + request_rejected_message
time.sleep(random.randint(8,25))

# Click submit
element = browser.find_element(By.ID, 'btnEntrar')
browser.execute_script("arguments[0].click();", element)

# ------------- Page 4 --------------------------
assert request_rejected_message not in browser.page_source, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " " + request_rejected_message
time.sleep(random.randint(8,25))

# Radio Button Click
browser.find_element(By.ID, 'rdbTipoDocPas').click()

time.sleep(random.randint(10,20))

# Send passport id
element = browser.find_element(By.ID, "txtIdCitado")
element.send_keys(passport)

time.sleep(random.randint(3,10))

# Send complete name
element = browser.find_element(By.ID, "txtDesCitado")
element.send_keys(full_name)

time.sleep(random.randint(3,10))

# Click submit
element = browser.find_element(By.ID, 'btnEnviar')
browser.execute_script("arguments[0].click();", element)

# ------------- Page 5 --------------------------
assert request_rejected_message not in browser.page_source, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " " + request_rejected_message
time.sleep(random.randint(8,25))

# Click submit
element = browser.find_element(By.ID, 'btnEnviar')
browser.execute_script("arguments[0].click();", element)



# ------------- Page 6 --------------------------

time.sleep(random.randint(8,25))

assert "En este momento no hay citas disponibles" not in browser.page_source
assert request_rejected_message not in browser.page_source, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " " + request_rejected_message
#---------------- Continue only if assert was a success ---------





# Set the subject and body of the email
subject = 'Alerte RDV NIE'
body = """
Rendez-vous trouvé dans les 10 minutes précédent ce mail, peut-être déjà réservé entre temps
"""
email_sender = 'perretrichard1996@gmail.com'
email_password = 'gwbrlkofikqvhpdm'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
    


    






    




# ======= Values =============

# ------------- Page 1 --------------------------
# Selection de la province
# <select id="form" name="form" autocomplete="address-level1">
#     <option value="/icpco/citar?p=3&amp;locale=es">Alicante</option>	  					
#     <option value="/icpplus/citar?p=46&amp;locale=es">Valencia</option>
# </select>

# click()
#<input id="btnAceptar" onclick="envia()" value="Aceptar" class="mf-button primary" type="button">

# ------------- Page 2 --------------------------

# <select name="sede" id="sede" data-live-search="true" title="Oficina" class="mf-input__xl" onchange="cargaTramites()">   
#     <option value="99">Cualquier oficina</option>
#     <optgroup label="Elegir oficina">
#         <option value="4">CNP-COMISARIA DE BAILEN, Bailen, 9</option>
#     </optgroup>
# </select>

# Timeout de 2 secondes pour que le js du site s'actualise
 
# <select name="tramiteGrupo[0]" id="tramiteGrupo[0]" onchange="eliminarSeleccionOtrosGrupos(0);cargaMensajesTramite()" class="mf-input__l">
#     <option value="-1" selected="selected">Despliegue para ver trámites disponibles en esta provincia</option>
#     <option value="4038">POLICIA-CERTIFICADO DE REGISTRO DE CIUDADANO DE LA U.E.</option>
# </select>

# <input id="btnAceptar" type="button" class="mf-button primary" value="Aceptar" onclick="envia()">

# ------------- Page 3 --------------------------

# <input id="btnEntrar" type="button" class="mf-button primary" value="Entrar" onclick="document.forms[0].submit()">

# ------------- Page 4 --------------------------

# <input type="radio" value="PASAPORTE" id="rdbTipoDocPas" onclick="invisibleNieYDniYColegiado()" name="rdbTipoDoc">

# <input type="text" id="txtIdCitado" size="9" maxlength="9" class="cajapeque" required="" name="txtIdCitado" value="" title="N.I.E.">
# name = "RICHARD PERRET"

# <input autocomplete="name" type="text" id="txtDesCitado" pattern="[a-zA-Z]*" onchange="comprobarDatos()" maxlength="50" class="mf-input__m" title="Nombre y apellidos" required="" name="txtDesCitado" value="">
# id_card = "160575M00860"

# <input id="btnEnviar" type="button" class="mf-button primary" value="Aceptar" onclick="envia()">

# ------------- Page 5 --------------------------

# <input id="btnEnviar" type="button" class="mf-button primary" value="Solicitar Cita" onclick="enviar('solicitud')">

# ------------- Page 6 --------------------------

# ???