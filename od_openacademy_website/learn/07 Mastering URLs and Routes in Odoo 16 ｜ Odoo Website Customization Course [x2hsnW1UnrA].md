example :

```python
    @http.route('/odoodiscussions/<string:name>', auth='public', website=True, type='http')  
    def display_name(self, name):
        return "This is Odoo Discussions with Name: %s" % name
    
    @http.route('/odoodiscussions/<int:my_id>', auth='public', website=True, type='http')  
    def display_id(self, my_id):
        return "This is Odoo Discussions with ID: %s" % my_id

```

Here is the extracted Odoo controller code from the images:

```python
from odoo import http
from odoo.http import request

class OpenAcademyWebsite(http.Controller):

    @http.route("/odoodiscussions/<model('od_openacademy.course'):course>", 
                auth='public', website=True, type='http')
    def display_name(self, course):
        template = "od_openacademy_website.odoodiscussions_course"
        return request.render(template, {'course': course})
```

### **Explanation:**
1. **Controller Definition:**
   ```python
   class OpenAcademyWebsite(http.Controller):
   ```
   - Defines a new controller class for handling website routes.

2. **Route Definition:**
   ```python
   @http.route("/odoodiscussions/<model('od_openacademy.course'):course>", 
                auth='public', website=True, type='http')
   ```
   - **`/odoodiscussions/<model('od_openacademy.course'):course>`**: 
     - Defines a dynamic URL that takes a course model record (`od_openacademy.course`) as a parameter.
     - Example URL: `/odoodiscussions/3` (where `3` is the course ID).
   - **`auth='public'`**: Allows public users to access this route.
   - **`website=True`**: Indicates that this is a website controller.
   - **`type='http'`**: This is an HTTP route (not JSON-RPC or other types).

3. **Controller Method (`display_name`)**
   ```python
   def display_name(self, course):
   ```
   - This method takes the `course` parameter, which is an instance of the `od_openacademy.course` model.

4. **Rendering the Template:**
   ```python
   template = "od_openacademy_website.odoodiscussions_course"
   return request.render(template, {'course': course})
   ```
   - **`template`**: Specifies which QWeb template to render (`odoodiscussions_course`).
   - **`request.render()`**: Renders the template and passes the `course` data.

---

### **Template Usage**
From the extracted template code:

```xml
<template id="odoodiscussions_classes" name="Odoo Discussions Classes">
    <t t-call="website.layout">
        <title>Odoo Discussions</title>
        <h2><span t-esc="message"/></h2>
        <ul>
            <t t-foreach="courses" t-as="course">
                <li>
                    <a t-attf-href="/odoodiscussions/{{ slug(course) }}">
                        <t t-esc="course.code"/>
                    </a>
                    <span t-field="course.name"/>
                </li>
            </t>
        </ul>
    </t>
</template>
```

#### **Explanation of the Template**
- **List of Courses (`t-foreach="courses"`)**:
  - Iterates over `courses` and creates a list item (`<li>`) for each course.
- **Course URL (`t-attf-href`)**:
  - Creates a link to `/odoodiscussions/<slug>` where `slug(course)` generates a readable URL.
- **Displays Course Code and Name**:
  - `t-esc="course.code"` → Displays the course code.
  - `t-field="course.name"` → Displays the course name.

---

### **How This Works in Odoo**
1. **A user visits `/odoodiscussions/3`**:
   - The controller fetches the course with ID `3`.
   - The `odoodiscussions_course` template is rendered with the course details.

2. **The course listing page**:
   - Displays a list of available courses.
   - Each course has a clickable link to its detailed page.

---

### **Conclusion**
- The controller handles course details dynamically using Odoo’s model-based routing.
- The templates generate a clean, user-friendly webpage for course listings and details.
- The use of `slug(course)` ensures SEO-friendly URLs.

Let me know if you need more explanations! 🚀


Here is the extracted code from the image:

```xml
<template id="odoodiscussions_classes" name="Odoo Discussions Classes">
    <t t-call="website.layout">
        <title>Odoo Discussions</title>
        <h2><span t-esc="course.name"/></h2>
        <h2><span t-esc="course.code"/></h2>
        <h2><span t-esc="course.responsible_id.name"/></h2>
    </t>
</template>
```

### **Explanation:**
1. **`<template>`**:
   - Defines a QWeb template with the ID `"odoodiscussions_classes"` and the name `"Odoo Discussions Classes"`.

2. **`<t t-call="website.layout">`**:
   - This template extends the default Odoo website layout.

3. **`<title>Odoo Discussions</title>`**:
   - Sets the title of the page to `"Odoo Discussions"`.

4. **Displaying Course Details**:
   - `<h2><span t-esc="course.name"/></h2>` → Displays the course name.
   - `<h2><span t-esc="course.code"/></h2>` → Displays the course code.
   - `<h2><span t-esc="course.responsible_id.name"/></h2>` → Displays the name of the person responsible for the course.

### **Usage in Odoo:**
- This template is used to display course details on the website.
- It is likely rendered by an Odoo controller that passes the `course` record.

Would you like help linking this to a controller or making modifications? 😊