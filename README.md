# Django Assignment: Building a Healthcare Backend

>> Not used PostgreSQL since it is behind ORM and it will easier to Test my Project for you.

## Overview

This API enables the management of patient-doctor mappings in a healthcare system. It uses **Django REST Framework (DRF)** with **JWT Authentication**, **Custom Serializers**, and **Class-Based Views (CBVs)** to handle patient assignments to doctors, with functionalities for **creating**, **retrieving**, and **deleting** patient-doctor relationships.

## Key Features

### 1. **JWT Authentication**
- Ensures secure access to the API by requiring users to provide a JWT token for authentication.

### 2. **Custom Serializers**
- Custom serializer (`MappingSerializer`) controls how patient-doctor relationships are serialized and deserialized.
- Uses `to_representation()` to define how related data (assigned doctors) is presented in the response.

### 3. **Class-Based Views (CBVs)**
- Utilizes DRF's **APIView** to structure views with methods corresponding to HTTP requests (`POST`, `GET`, `DELETE`).
- Methods handle data creation, retrieval, and deletion for patient-doctor mappings.

### 4. **Many-to-Many Relationships**
- **Patient** and **Doctor** models are linked via a **many-to-many relationship**. The serializer reflects this by displaying doctors assigned to each patient.

### 5. **Error Handling**
- Proper error handling is in place, returning clear error messages (e.g., `Doctor not found`).

### 6. **Dynamic Data Fetching**
- Supports retrieving a **single patient’s mapping** or all patients' mappings dynamically based on the presence of `patient_id`.

### 7. **Permissions**
- **Permissions** ensure only authenticated users or users with specific roles (like `IsOfficer`) can access certain views.



## Conclusion

This API provides a simple yet scalable way to manage patient-doctor mappings in a healthcare setting. With **JWT Authentication**, **Custom Serializers**, **DRF CBVs**, and a clean approach to **error handling** and **dynamic data fetching**, it ensures secure, efficient management of healthcare data.

