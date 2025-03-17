Here is the extracted code from the images for **creating breadcrumbs in Odoo Website Portal**:

---

### **1. Breadcrumb for Course Navigation**
```xml
    <template id="portal_my_home_menu_course" name="Portal layout: openacademy menu entries"
        inherit_id="portal.portal_breadcrumbs">
        <xpath expr="//ol[hasclass('o_portal_submenu')]" position="inside">
            <li t-if="page_name == 'course'"
                t-attf-class="breadcrumb-item #{'active ' if not course else ''}">
                <a t-if="course" t-attf-href="/odoodiscussions/classes?{{ keep_query() }}">
                    Courses
                </a>
                <t t-else="">Courses</t>
            </li>
            <li t-if="course" class="breadcrumb-item active">
                <t t-out="course.name" />
            </li>
        </xpath>
    </template>
```

---

### **Explanation:**
📌 **Extends `portal.portal_my_home`** to modify the breadcrumb section.  
📌 Uses `xpath` to inject new elements inside the `<ol>` tag that has the class `"o_portal_submenu"`.

#### **Breadcrumb Logic:**
- **If `page_name == 'course'`**, it adds a breadcrumb **"Courses"**.
  ```xml
  <li t-if="page_name == 'course'" 
      t-attf-class="breadcrumb-item #{'active ' if not course else ''}">
  ```
  - **If a specific course is not selected**, `"Courses"` is **active**.
  - **If a course is selected**, `"Courses"` links to `/odoodiscussions/classes`.

- **If a specific `course` exists**, it displays the course name.
  ```xml
  <li t-if="course" class="breadcrumb-item active">
      <t t-out="course.name"/>
  </li>
  ```
  - This makes the **course name** appear in the breadcrumb.

---

### **2. Sidebar Template for Course Details**
```xml
<template id="portal_my_course" name="My Course" inherit_id="portal.portal_sidebar" primary="True">
    <xpath expr="//div[hasclass('o_portal_sidebar')]" position="inside">
        <title>Odoo Discussions</title>
        <h2> <span t-esc="course.name"/> </h2>
        <h2> <span t-esc="course.code"/> </h2>
        <h2> <span t-esc="course.responsible_id.name"/> </h2>
    </xpath>
</template>
```

---

### **Explanation:**
📌 **Extends `portal.portal_sidebar`** to add **course details** to the sidebar.  
📌 Uses `xpath` to inject elements inside the `<div>` that has class `"o_portal_sidebar"`.

#### **What it Displays?**
- **Course Name:** `<h2> <span t-esc="course.name"/> </h2>`
- **Course Code:** `<h2> <span t-esc="course.code"/> </h2>`
- **Responsible Person (Instructor/Admin):**  
  ```xml
  <h2> <span t-esc="course.responsible_id.name"/> </h2>
  ```

---

### **How It Works in Odoo Portal**
1. **User Navigates to Course Page** (`/odoodiscussions/classes/{course_id}`)
2. **Breadcrumb Appears at the Top**
   - If in **course list**, it shows **"Courses"**.
   - If in **a specific course**, it shows `"Courses > Course Name"`.
3. **Sidebar Shows Course Details**
   - Displays the course name, code, and responsible person.

---

### **Enhancements & Suggestions**
✅ **Make "Courses" Breadcrumb Link Dynamic**  
Change:
```xml
<a t-if="course" t-attf-href="/odoodiscussions/classes?{{ keep_query() }}">
```
To:
```xml
<a t-if="course" t-attf-href="/odoodiscussions/{{ course.id }}">
```
*(So users can navigate to the course page directly.)*

✅ **Add More Course Details in Sidebar**  
Example:
```xml
<h2> <span t-esc="course.duration"/> Hours</h2>
```

---

### **Final Thoughts**
✅ **This adds a dynamic breadcrumb system to the Odoo portal.**  
✅ **It integrates with the sidebar to show course details.**  
✅ **Improves User Navigation & UX in Odoo Discussions Portal.**  

🚀 *Would you like further improvements or styling suggestions?* 😊