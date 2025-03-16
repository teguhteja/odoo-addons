Here is the extracted **Odoo website menu and page code** from the images:

---

### **1. Website Menu (`views/menu.xml`)**
This code adds a new menu item **"About Us"** to the Odoo website.

```xml
<odoo>
    <data>
        <record id="menu_aboutus" model="website.menu">
            <field name="name">About us</field>
            <field name="url">/aboutus</field>
            <field name="page_id" ref="od_openacademy_website.aboutus_page"/>
            <field name="parent_id" ref="website.main_menu"/>
            <field name="sequence" type="int">50</field>
        </record>
    </data>
</odoo>
```

### **Explanation:**
- **`id="menu_aboutus"`** → Unique ID for the menu item.
- **`model="website.menu"`** → Defines a menu in the Odoo website.
- **`<field name="name">About us</field>`** → Sets the menu name as **"About us"**.
- **`<field name="url">/aboutus</field>`** → The URL for the menu item.
- **`<field name="page_id" ref="od_openacademy_website.aboutus_page"/>`** → Links this menu to the **About Us** page.
- **`<field name="parent_id" ref="website.main_menu"/>`** → Places it under the main website menu.
- **`<field name="sequence" type="int">50</field>`** → Defines the order of the menu item.

---

### **2. Website Page (`views/aboutus_page.xml`)**
This code defines the **About Us** page content.

```xml
<odoo>
    <data>
        <template id="about_us_page" name="About Us Page">
            <t t-call="website.layout">
                <div class="container mt-5">
                    <div class="text-center">
                        <h1>About Us</h1>
                        <p>Welcome to <strong>Odoo Discussions</strong>, your go-to channel for learning Odoo!</p>
                    </div>
                    <div class="mt-4">
                        <h2>What We Offer</h2>
                        <ul>
                            <li>Step-by-step guides on Odoo installation and development</li>
                            <li>Comprehensive courses on Odoo customization</li>
                            <li>Expert tips and tricks for developers</li>
                        </ul>
                    </div>
                    <div class="mt-4">
                        <h2>Subscribe to Our YouTube Channel</h2>
                        <p>Visit our YouTube channel: 
                            <a href="https://www.youtube.com/@odoodiscussions" target="_blank">
                                Odoo Discussions
                            </a>
                        </p>
                    </div>
                </div>
            </t>
        </template>

        <record id="aboutus_page" model="website.page">
            <field name="url">/aboutus</field>
            <field name="is_published">True</field>
            <field name="view_id" ref="about_us_page"/>
        </record>
    </data>
</odoo>
```

### **Explanation:**
- **Template (`id="about_us_page"`)**
  - Uses **`t-call="website.layout"`** to apply Odoo's default website layout.
  - Displays a **title**, **description**, **offerings**, and a **YouTube link**.

- **Website Page (`id="aboutus_page"`)**
  - **`<field name="url">/aboutus</field>`** → Defines the page URL.
  - **`<field name="is_published">True</field>`** → Ensures the page is visible to users.
  - **`<field name="view_id" ref="about_us_page"/>`** → Links the page to the template.

---

### **3. How It Works**
- When users visit **`/aboutus`**, the **About Us page** is displayed.
- The **menu item "About Us"** appears in the **main website navigation**.
- Clicking on the **menu item** redirects users to the **About Us page**.

---

### **4. How to Install in Odoo**
1. **Ensure your module's `__manifest__.py` includes:**
   ```python
   {
       'name': 'OpenAcademy Website',
       'version': '1.0',
       'category': 'Website',
       'summary': 'Odoo Discussions Website Pages',
       'depends': ['website'],
       'data': [
           'views/menu.xml',
           'views/aboutus_page.xml',
       ],
       'installable': True,
       'application': True,
   }
   ```
2. **Restart Odoo and update your module:**
   ```sh
   ./odoo-bin -c odoo.conf -u od_openacademy_website
   ```
3. **Go to Website → Refresh Menu**
   - The **"About Us"** menu should now appear.
   - Clicking it should display the **About Us** page.

---

### **Final Output**
- **Menu:** "About Us" appears in the Odoo website menu.
- **Page:** `/aboutus` displays detailed information about **Odoo Discussions**.
- **Link:** The page includes a **YouTube subscription link**.

This setup ensures **a fully functional website page with a navigation menu** in Odoo. 🚀 Let me know if you need any modifications!


Here is the extracted **Odoo website menu XML code** from the image:

```xml
<record id="menu_openacademy" model="website.menu">
    <field name="name">OpenAcademy</field>
    <field name="website_id" ref="website.default_website"/>
    <field name="parent_id" search="[('parent_id', '=', False), ('website_id', '=', 1)]"/>
    <field name="sequence" type="int">40</field>
</record>

<record id="menu_classes" model="website.menu">
    <field name="name">Classes</field>
    <field name="url">/odoodiscussions/classes</field>
    <field name="parent_id" ref="od_openacademy_website.menu_openacademy"/>
    <field name="website_id" ref="website.default_website"/>
    <field name="sequence" type="int">10</field>
</record>
```

---

### **Explanation:**
1. **Main Menu: "OpenAcademy"**
   ```xml
   <record id="menu_openacademy" model="website.menu">
   ```
   - This defines the **main menu** item **"OpenAcademy"**.

   ```xml
   <field name="parent_id" search="[('parent_id', '=', False), ('website_id', '=', 1)]"/>
   ```
   - It ensures that the menu is at the **top-level** of the website navigation.

2. **Sub Menu: "Classes"**
   ```xml
   <record id="menu_classes" model="website.menu">
   ```
   - This creates a **submenu item** under "OpenAcademy".

   ```xml
   <field name="parent_id" ref="od_openacademy_website.menu_openacademy"/>
   ```
   - **This sets "Classes" as a child menu under "OpenAcademy".**

   ```xml
   <field name="url">/odoodiscussions/classes</field>
   ```
   - Clicking on "Classes" redirects the user to the `/odoodiscussions/classes` page.

3. **Website Association**
   ```xml
   <field name="website_id" ref="website.default_website"/>
   ```
   - Both menus belong to the **default Odoo website**.

4. **Menu Order**
   ```xml
   <field name="sequence" type="int">40</field>
   <field name="sequence" type="int">10</field>
   ```
   - The **"OpenAcademy" menu** appears **before "Classes"** due to its sequence.

---

### **How It Works**
- **"OpenAcademy"** appears as a top-level website menu.
- **"Classes"** appears as a submenu under "OpenAcademy".
- Clicking **"Classes"** navigates to `/odoodiscussions/classes`.

---

### **How to Install in Odoo**
1. **Add this XML file to your module (`views/menu.xml`):**
2. **Update the `__manifest__.py` file:**
   ```python
   {
       'name': 'OpenAcademy Website',
       'version': '1.0',
       'category': 'Website',
       'depends': ['website'],
       'data': [
           'views/menu.xml',
       ],
       'installable': True,
       'application': True,
   }
   ```
3. **Restart Odoo and update your module:**
   ```sh
   ./odoo-bin -c odoo.conf -u od_openacademy_website
   ```
4. **Go to Website → Refresh Menu**
   - The **"OpenAcademy"** menu should now appear.
   - Hover over **"OpenAcademy"**, and **"Classes"** will be visible as a submenu.

---

### **Expected Website Menu Output**
```
OpenAcademy ▼
    ├── Classes  (Linked to /odoodiscussions/classes)
```

This setup ensures a **proper hierarchical menu structure** for your Odoo website. 🚀 Let me know if you need modifications!