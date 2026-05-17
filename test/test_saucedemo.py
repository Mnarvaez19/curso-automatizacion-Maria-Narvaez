from selenium.webdriver.chrome.webdriver import WebDriver

from funciones.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login( driver: WebDriver ):
    login(driver , "standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"


def test_catalogo_productos( driver: WebDriver ):
    login(driver , "standard_user", "secret_sauce")

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

    #validar productos
    productos = driver.find_elements(By.CSS_SELECTOR, " [data-test='inventory-item']")
    assert len(productos) > 0
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre == "Sauce Labs Backpack"

    # Verificar visibilidad de Menú y Filtro
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        
    assert menu.is_displayed()
    assert filtro.is_displayed()

def test_agregar_al_carrito( driver: WebDriver ):
    login(driver , "standard_user", "secret_sauce")
    wait = WebDriverWait(driver , 10)

    nombre_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    #agregar productos 
    bnt_add = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
    )    
    bnt_add.click()

    #validar contador 
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #validar productos en el carrito 
    producto_carrito = driver.find_element(By. CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == nombre_producto