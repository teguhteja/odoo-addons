Here is the extracted Odoo website portal code from the images:

```xml
<template id="portal_my_classes" name="My Quotations">
    <t t-call="portal.portal_layout">
        <t-set="breadcrumbs_searchbar" t-value="True"/>
        
        <t-call="portal.portal_searchbar">
            <t t-set="title">Classes</t>
        </t-call>

        <t t-if="courses" t-call="portal.portal_table">
            <thead>
                <tr class="active">
                    <th>Course #</th>
                    <th class="text-end">Course Name</th>
                    <th class="text-end">Course Date</th>
                    <th class="text-end">Status</th>
                </tr>
            </thead>
            <t t-foreach="courses" t-as="course">
                <tr>
                    <td>
                        <a t-attf-href="/odoodiscussions/{{ slug(course) }}">
                            <t t-esc="course.code"/>
                        </a>
                    </td>
                    <td class="text-end"><span t-field="course.name"/></td>
                    <td class="text-end"><span t-field="course.course_date"/></td>
                    <td class="text-end">
                        <span t-field="course.state"/>
                    </td>
                </tr>
            </t>
        </t>

        <p t-else="">There are currently no courses for your account.</p>
    </t>
</template>
```

---

### **Explanation of the Code:**
This **Odoo QWeb template** adds a **"Classes"** section to the customer portal. It displays **a list of courses** a user is enrolled in.

#### **1. Defining the Template**
```xml
<template id="portal_my_classes" name="My Quotations">
```
- **`id="portal_my_classes"`** → Unique identifier for this portal template.
- **`name="My Quotations"`** → This name might need changing to **"My Classes"** to reflect the section’s purpose.

---

#### **2. Extending the Portal Layout**
```xml
<t t-call="portal.portal_layout">
```
- Uses the **default Odoo portal layout** for consistent styling.

---

#### **3. Adding a Search Bar**
```xml
<t-set="breadcrumbs_searchbar" t-value="True"/>
<t-call="portal.portal_searchbar">
    <t t-set="title">Classes</t>
</t-call>
```
- Enables **breadcrumbs & search bar** at the top of the page.
- Sets **"Classes"** as the title.

---

#### **4. Checking if Courses Exist**
```xml
<t t-if="courses" t-call="portal.portal_table">
```
- If **courses exist**, display them in a **table** (`portal.portal_table`).

---

#### **5. Creating the Table Header**
```xml
<thead>
    <tr class="active">
        <th>Course #</th>
        <th class="text-end">Course Name</th>
        <th class="text-end">Course Date</th>
        <th class="text-end">Status</th>
    </tr>
</thead>
```
- Defines **column headers**:
  - **Course #**
  - **Course Name**
  - **Course Date**
  - **Status**

---

#### **6. Looping Through Courses**
```xml
<t t-foreach="courses" t-as="course">
    <tr>
        <td>
            <a t-attf-href="/odoodiscussions/{{ slug(course) }}">
                <t t-esc="course.code"/>
            </a>
        </td>
        <td class="text-end"><span t-field="course.name"/></td>
        <td class="text-end"><span t-field="course.course_date"/></td>
        <td class="text-end">
            <span t-field="course.state"/>
        </td>
    </tr>
</t>
```
- Iterates over **`courses`**.
- Generates **a clickable Course #** that links to `/odoodiscussions/{{ slug(course) }}`.
- Displays:
  - **Course Name**
  - **Course Date**
  - **Course Status**

---

#### **7. Handling No Courses Available**
```xml
<p t-else="">There are currently no courses for your account.</p>
```
- If **no courses exist**, display **a message**.

---

### **How This Works in Odoo:**
1. **User logs into the portal**.
2. **The "Classes" page** displays a **list of courses** they are enrolled in.
3. If no courses exist, they see **"There are currently no courses for your account."**
4. **Each course links to `/odoodiscussions/{{ slug(course) }}`**, where they can view more details.

---

### **Enhancements & Suggestions**
✅ **Make "My Quotations" → "My Classes"**
```xml
<template id="portal_my_classes" name="My Classes">
```

✅ **Show the Course Count in the Title**
Modify the title to display the course count dynamically:
```xml
<t t-set="title">Your Classes (<t t-esc="len(courses)"/>)</t>
```

✅ **Add a Button to Enroll in New Classes**
```xml
<a class="btn btn-primary" href="/enroll">Enroll in a Class</a>
```

---

### **Final Thoughts**
📌 **This portal page lists the user's courses dynamically.**  
📌 **It uses Odoo’s portal layout for consistency.**  
📌 **If no courses exist, it displays a fallback message.**  

🚀 *Would you like help integrating this with your controller or making further improvements?* 😊