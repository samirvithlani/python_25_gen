from playwright.sync_api import sync_playwright

#https://www.myntra.com/men-tshirts
product ={}
with sync_playwright() as p:
    #headless= true -->browser bg open..
    browser =p.chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")
    #page.wait_for_timeout(4000)
    title = page.title()
    print("title = ",title)
    
    books = page.locator("article.product_pod")
        
    print(books)
    for i  in range(books.count()):
        book = books.nth(i)
        title =book.locator("h3 a").get_attribute("title")
        price = book.locator(".price_color").inner_text()
        avaialbilty = book.locator(".instock").inner_text()
        #print(f"title = {title} price = {price} avail = {avaialbilty}")
        product[i] = [{"title":title,"availablity":avaialbilty,"price":price}]
        
    # page.wait_for_timeout(4000)
    browser.close()

print(product)    