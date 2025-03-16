1
- create usings scaffold od_openacademy_website
- edit manifest

- Here is the extracted text from the Odoo website controller in the image:

```python
from odoo import http

class OdooDiscussions(http.Controller):

    @http.route('/odoodiscussions/courses', auth='public', website=True)
    def display_data(self, **kwargs):
        return "This is Odoo Discussions"
```

### Explanation:
This code defines a simple Odoo website controller:

1. **Importing HTTP Controller**  
   ```python
   from odoo import http
   ```
   - This imports the necessary `http` module from Odoo to create a controller.

2. **Creating a Controller Class**  
   ```python
   class OdooDiscussions(http.Controller):
   ```
   - Defines a controller class named `OdooDiscussions`, inheriting from `http.Controller`.

3. **Defining a Route**  
   ```python
   @http.route('/odoodiscussions/courses', auth='public', website=True)
   ```
   - This creates a route accessible at `/odoodiscussions/courses`.
   - `auth='public'` allows anyone (even unauthenticated users) to access the route.
   - `website=True` ensures that this route is part of the Odoo website module.

4. **Defining a Method to Return Data**  
   ```python
   def display_data(self, **kwargs):
       return "This is Odoo Discussions"
   ```
   - This method handles requests to the defined route and returns a simple text response:  
     **"This is Odoo Discussions"**.

### How to Access:
- If this module is installed and running in Odoo, visit:  
  **http://your-odoo-domain/odoodiscussions/courses**  
  - You should see **"This is Odoo Discussions"** displayed in your browser.

Let me know if you need further clarifications! 🚀

Here is the extracted text from the Odoo Python controller in the image:

```python
@http.route('/odoodiscussions/sessions', auth='public', website=True)
def display_sessions(self, **kwargs):
    return "This is Odoo Discussions Sessions"
```

### Explanation:

1. **Route Definition:**
   ```python
   @http.route('/odoodiscussions/sessions', auth='public', website=True)
   ```
   - This creates a web route at `/odoodiscussions/sessions`.
   - `auth='public'` allows access without authentication.
   - `website=True` ensures this is a website route in Odoo.

2. **Function Handling the Route:**
   ```python
   def display_sessions(self, **kwargs):
   ```
   - Defines a function named `display_sessions` to handle requests to the route.

3. **Returning a Response:**
   ```python
   return "This is Odoo Discussions Sessions"
   ```
   - When the route is accessed, it returns a simple text response:  
     **"This is Odoo Discussions Sessions"**.

### How to Access:
If this module is installed and running in Odoo, visit:
```
http://your-odoo-domain/odoodiscussions/sessions
```
You should see:
```
This is Odoo Discussions Sessions
```

Let me know if you need further details! 🚀