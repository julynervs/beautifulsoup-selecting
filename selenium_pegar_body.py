def selecionar_aba(driver, aba):
    try:
        driver.switch_to.window(driver.window_handles[aba])
    except IndexError as e:
        print("ERRO ao ", "Existe somente uma aba aberta, e será copiado apenas o HTML da segunda aba")

def retornar_body(driver, url="", definir_url=False):
    if definir_url == True:
        driver.get(url)
    try:
        body = driver.find_element_by_tag_name("body")
        body = body.get_attribute('innerHTML')
        url = driver.current_url
    except Exception as e:
        print(f"Um outro erro aconteceu ERRO: {e}")
    else:
        return url, body