Here is the extracted Odoo controller code from the images:

```python
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomerPortalDiscussions(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        print(values, "VALUESSssssssssssssssss")
        print(counters, "COUNTERSSssssssssssssssss")
        return values
```

---

### **Explanation of the First Code Snippet:**
- **`CustomerPortalDiscussions`**: This class extends Odoo's **CustomerPortal** to add custom portal values.
- **`_prepare_home_portal_values(self, counters)`**:
  - **Overrides** the parent method from `CustomerPortal`.
  - Calls the **super method** using:
    ```python
    values = super()._prepare_home_portal_values(counters)
    ```
    This fetches the default portal values.
  - **Debugging Prints**:
    ```python
    print(values, "VALUESSssssssssssssssss")
    print(counters, "COUNTERSSssssssssssssssss")
    ```
    - Prints `values` and `counters` to help debug what data is passed.

---

### **Updated Code (From Second Image):**
```python
class CustomerPortalDiscussions(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['course_count'] = request.env['od_openacademy.course'].search_count([])
        return values
```

#### **What Changed?**
1. **Added Course Count Calculation**
   ```python
   values['course_count'] = request.env['od_openacademy.course'].search_count([])
   ```
   - Queries **how many courses** exist in `od_openacademy.course`.
   - Adds the count to `values` under the key `'course_count'`.

2. **Now the `values` Dictionary Includes:**
   - **Default Portal Values** from `CustomerPortal`
   - **`course_count`** → The total number of courses

---

### **How It Works in Odoo Portal**
- **Users visit their portal dashboard**.
- `_prepare_home_portal_values`:
  - **Retrieves the default portal values** (from `super()`).
  - **Adds the number of courses** (`course_count`).
- **The `course_count` is displayed in the portal UI** (if referenced in templates).

---

### **Use Case:**
- This modification **enhances** the customer portal by showing the **number of courses** a user can access.
- It can be used in **portal templates** like:
  ```xml
  <t t-esc="values.get('course_count', 0)"/>
  ```
  *(Displays the course count in the UI.)*

---

### **Possible Enhancements:**
✅ **Filter Courses by Logged-in User:**
```python
values['course_count'] = request.env['od_openacademy.course'].search_count([
    ('user_id', '=', request.env.user.id)
])
```
*(Only counts courses assigned to the current user.)*

✅ **Add More Counters (e.g., Assignments, Discussions, etc.)**
```python
values['assignment_count'] = request.env['od_openacademy.assignment'].search_count([])
```

---

### **Final Thoughts**
- This **extends the Odoo Portal Homepage** by **displaying the number of courses**.
- Uses **Odoo ORM (`search_count([])`)** to fetch data dynamically.
- Can be further **customized** to show user-specific data.

Would you like to integrate this with an Odoo template or improve it further? 😊🚀