# Selenium Cucumber Python - Project Overview

## Tech Stack
- **Language:** Python
- **BDD Framework:** Behave (same as Cucumber in Java)
- **Browser Automation:** Selenium WebDriver
- **Reporting:** Allure Reports
- **Application Tested:** SmartInventory (React Login Page)

---

## Folder Structure

### 1. Features (`features/`)
Contains `.feature` files written in **Gherkin language** (plain English test scenarios).
- `Feature` — groups related test cases
- `Background` — runs before every scenario (like `@Before` in Java)
- `Scenario` — a single test case
- `Scenario Outline` — data-driven testing using `Examples` table
- `@smoke`, `@regression` — tags to filter which tests to run

### 2. Pages (`pages/`)
Follows the **Page Object Model (POM)** design pattern.
- Each web page has its own Python class
- Contains locators (XPath, ID, CSS) and action methods
- Keeps test logic separate from page interactions
- Same concept as `LoginPage.java` in Java Selenium

### 3. Runner
In Java you have a `CucumberRunner.java` class. In Python Behave, the **`behave` CLI command** acts as the runner.
```bash
behave                    # run all tests
behave --tags=smoke       # run only smoke tests
behave --tags=regression  # run only regression tests
```

### 4. Steps (`steps/`)
Contains **step definition files** — the glue code connecting Gherkin steps to Selenium actions.
- `@given` → setup (open browser, navigate to URL)
- `@when` → actions (enter username, password, click login)
- `@then` → assertions (verify page title or success message)
- `context.driver` is the shared WebDriver instance (like dependency injection in Java)

### 5. Utilities (`utilities/`)
Reusable helper classes used across the framework:
- **DriverFactory** — creates and manages WebDriver instance
- **ConfigReader** — reads URLs, credentials from a config file
- **WaitHelper** — explicit waits (`WebDriverWait`)
- Same pattern as `DriverFactory.java`, `ConfigReader.java` in Java
