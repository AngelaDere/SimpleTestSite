class TestSettings:
    page_url = 'http://simpletestsite.fabrykatestow.pl'

    # Basic Auth Tab
    id_auth_tab = "basicauth-header"
    id_auth_content = "basicauth-content"
    id_auth_username = "ba_username"
    id_auth_password = "ba_password"
    xpath_auth_login_button = "//button[@onclick='onLoginSubmit()']"
    id_auth_logged_in = "loggedInMessage"
    logged_in_auth_text = "You are logged in!"
    login_form_auth_error = "Invalid credentials"

    # Form Tab
    id_form_tab = "form-header"
    id_form_content = "form-content"
    id_form_first_name = "fname"
    id_form_last_name = "lname"
    id_form_submit_button = "formSubmitButton"
    info_form_text = "Please fill in this field."
    info_form_text_headless = "Please fill out this field."
    alert_form_text = "success"

    # Dropdown List Tab
    id_dropdown_tab = "dropdownlist-header"
    id_dropdown_content = "dropdownlist-content"
    id_dropdown_list = "dropdown"
    dropdown_options = ["Option 1", "Option 2"]
    dropdown_default_choice = "Please select an option"

    # Drag And Drop Tab
    id_drag_and_drop_tab = "draganddrop-header"
    id_drag_and_drop_content = "draganddrop-content"
    xpath_drag_and_drop_column_a = "//header[normalize-space()='A']"
    xpath_drag_and_drop_column_b = "//header[normalize-space()='B']"






