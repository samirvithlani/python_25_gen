from playwright.sync_api import sync_playwright

url = "https://www.myntra.com/men-tshirts"
product ={}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    
    
    
    for i in range(1,10):
        products = page.locator(".product-base")
        
        for i in range(products.count()):
            prod = products.nth(i)
            brand = prod.locator(".product-productMetaInfo .product-brand").inner_text()
            print(brand)
            price_locator = prod.locator(".product-productMetaInfo .product-price")
            price = price_locator.inner_text()
            #price = prod.locator(".product-productMetaInfo .product-price").inner_text()
            #discounted_price =price_locator.locator(".product-discountedPrice")
            discounted_price =price_locator.locator(".product-discountedPrice")
            dp = discounted_price.inner_text() if discounted_price.count()>0 else "N/A"
            print(price," - ",dp)
            # if discounted_price.count()>0:
            #     print(price," -",discounted_price.inner_text())
            # else:
            #     print("N/A")            
            
        
            
        next_button = page.locator(".pagination-next")
        if next_button.count()>0 and next_button.is_enabled():
            next_button.click()
            #page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(4000)
            
                
        else:
            print("next button is not available")
            
            
            
            
            
        
        
    browser.close()