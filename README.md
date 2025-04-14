# Ramen Nakama - Project Overview

<img src="media/ramen-responsive.jpg" alt="Ramen Nakama Homepage" width="1000">
<p style="font-size: 10px">Image Source: <a href="https://thebristolsauce.substack.com/p/ramen-nakama-the-scrandit-serious">Scrandit via The Bristol Sauce</a></p>

**Ramen Nakama** is a Django-based web application that enables customers to browse and order products and superuser (in this case, the store owner) to manage products, delivery windows and reviews. MENTION BUILT IN AT PRESENT UNUSED FEATURES - RATING ETC

The project utilizes modern web technologies including Django, Heroku, AWS S3 for static/media storage, and Stripe for payment processing. With a responsive, Bootstrap-powered front-end and custom CSS styling, Ramen Nakama offers a seamless user experience for customers and robust management tools for administrators.

[View Site Here](https://milestone-four-ff783f75758e.herokuapp.com)

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Design and Development Tools](#design-and-development-tools)
- [Usage Instructions](#usage-instructions)
  - [For Customers](#for-customers)
  - [For Staff/Admin](#for-staffadmin)
- [Testing](#testing)
- [Testing Table](#testing-table)
- [User Stories](#user-stories)
- [Visual Design](#visual-design)
- [Design Considerations](#design-considerations)
- [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
- [Essential Future Improvements](#essential-future-improvements)
- [Other Future Improvements](#other-future-improvements)
- [References and Credits](#references-and-credits)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **User-friendly Ordering:**  
  - Browse a selection of authentic ramen dishes, sides and merchandise (products to be added).
  - Add items to a shopping bag and check out seamlessly.
  
- **Review & Feedback System:**  
  - Customers can submit reviews (with an approval flow).
  - A dedicated “thank you” page for review submissions.

- **Dynamic News & Updates:**  
  - The homepage displays a summary of the latest news, managed by the superuser in the admin panel.
  - A news archive featuring an alternating two-column layout for images and text.

- **Responsive and Modern Design:**  
  - Built with Bootstrap 4 and enhanced with custom CSS.
  - Fully responsive layout for desktop, tablet, and mobile devices.

- **Secure Payment Processing:**  
  - Integrated with Stripe to handle payment intents and charge events.
  - Real-time triggers for key payment events.

---

## Technologies Used

#### Backend & Deployment  
[![Django](https://img.shields.io/badge/Django-3.2-green?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Heroku](https://img.shields.io/badge/Heroku-Deploy-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/)
[![AWS S3](https://img.shields.io/badge/AWS_S3-Storage-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/s3/)
[![Stripe](https://img.shields.io/badge/Stripe-Payments-6772e5?style=for-the-badge&logo=stripe&logoColor=white)](https://stripe.com/)

#### Frontend Technologies  
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4-563d7c?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

#### Database Solutions  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)

---

## Design and Development Tools

#### Code Editors & Version Control  
[![VSCode](https://img.shields.io/badge/VSCode-Editor-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

#### Design & Branding  
[![Figma](https://img.shields.io/badge/Figma-Design-F24E1E?style=for-the-badge&logo=figma&logoColor=white)](https://www.figma.com/)
[![Adobe Photoshop](https://img.shields.io/badge/Adobe%20Photoshop-31A8FF?style=for-the-badge&logo=adobe-photoshop&logoColor=white)](https://www.adobe.com/products/photoshop.html)
[![Font Awesome](https://img.shields.io/badge/Font%20Awesome-528DD7?style=for-the-badge&logo=font-awesome&logoColor=white)](https://fontawesome.com/)
[![Adobe Fonts](https://img.shields.io/badge/Adobe%20Fonts-000000?style=for-the-badge&logo=adobe&logoColor=white)](https://fonts.adobe.com/)

---

## Usage Instructions

### For Customers
- **Browse & Order:**  
  Visit the homepage to explore our ramen menu.  
  Add items to your bag and complete the checkout process easily.

- **Review Products:**  
  After receiving your order, you can submit a review from the review submission page.

<img src="#" alt="Customer ordering" width="800">

### For Staff/Admin
- **Admin Interface:**  
  Log in via the admin portal to manage products, view orders, and oversee reviews.
  
- **Content Updates:**  
  Use the integrated admin panels to add news items, update menus, and process user feedback.

<img src="#" alt="Admin interface" width="800">

---

## Testing

The project has been manually tested across various browsers and devices. Key scenarios included:
- Ordering flow from product selection to checkout.
- Review submission process with redirection to a thank-you page.
- Payment processing simulation using Stripe triggers.
- Responsiveness across desktop, tablet, and mobile viewports.

---

## Testing Table

| Test Condition                   | Expected Outcome                                  | Result   | Notes                      |
|----------------------------------|---------------------------------------------------|----------|----------------------------|
| Ordering a selection             | Items added and checkout processed correctly      | Pass/Fail| Checked with multiple items|
| Review Submission                | User is redirected to a thank-you page            | Pass/Fail|                            |
| Responsive layout                | Layout adjusts to mobile, tablet, and desktop     | Pass/Fail| Minor spacing adjustments  |
| Stripe payment simulation        | Payment events trigger correctly                  | Pass/Fail| Logged via Stripe dashboard|

---

## User Stories

- **As a customer, I want to order ramen quickly and easily**  
  - *Acceptance Criteria:* Fast ordering, clear product information, secure payment.
  
- **As a customer, I want to submit a review after my order**  
  - *Acceptance Criteria:* Review form validates input, shows success message.
  
- **As an admin, I want to manage news items and orders**  
  - *Acceptance Criteria:* Admin panel allows creating, updating, and deleting content.

---

## Visual Design

- **Layout:**  
  A grid-based, two-column layout for content pages with alternating news items.
  
- **Color Scheme:**  
  Utilizes Ramen Blue (#1e234d), Ramen Pink (#e75b66), and Ramen Yellow (#fde9d0) for a cohesive brand feel.
  
- **Typography:**  
  Custom fonts such as Skia CC in various weights (Regular, Bold, Condensed, etc.) are used across the site.

<img src="assets/images/design_placeholder.jpg" alt="Design overview" width="400">

---

## Design Considerations

- **Architectural Decisions:**  
  Modular Django apps for scalability and maintainability.
  
- **Responsive Design:**  
  Bootstrap 4 ensures the site adapts to all device types.
  
- **User Experience:**  
  Minimal clicks for ordering and submitting reviews with clear feedback.

- **Deployment & Maintenance:**  
  Deployed on Heroku, with AWS S3 for static and media file hosting.

---

## Entity Relationship Diagram (ERD)

<img src="assets/images/erd_placeholder.jpg" alt="ERD diagram" width="600">

**Explanation:**
- **Products:** Contains details about each ramen dish.
- **Orders:** Captures order details and status.
- **Reviews:** Stores customer reviews with a moderation flag.
- **News:** Maintains news updates for the site.

---

## Essential Future Improvements

- **Enhanced Payment Flow:**  
  Integrate more robust error handling and notifications for payment issues.
  
- **Mobile Optimization:**  
  Further refine mobile UX beyond Bootstrap defaults.
  
- **User Account Features:**  
  Implement wishlists and order tracking.

---

## Other Future Improvements

- **New Content Types:**  
  Ideas for Mailing List integration and additional user feedback models.
  
- **Real-time Updates:**  
  Consider WebSockets or AJAX for live order tracking and notifications.

---

## References and Credits

- **Django Documentation:** [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **Stripe API Reference:** [https://stripe.com/docs/api](https://stripe.com/docs/api)
- **Bootstrap Documentation:** [https://getbootstrap.com/](https://getbootstrap.com/)
- **Scrandit Image Source:** [https://thebristolsauce.substack.com/p/ramen-nakama-the-scrandit-serious](https://thebristolsauce.substack.com/p/ramen-nakama-the-scrandit-serious)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- **Mentor:** Special thanks to [Your Mentor's Name] for guidance.
- **Team Members:** Thanks to [Name 1], [Name 2], and [Name 3] for their contributions.
- **Inspiration:** Inspired by local Bristol cuisine culture and innovative delivery concepts.

---

### NOTES:

- **Webhook Testing for Stripe:**  
  - `stripe trigger payment_intent.created`  
  - `stripe trigger payment_intent.succeeded`  
  - `stripe trigger payment_intent.payment_failed`  
  - `stripe trigger charge.succeeded`  
  - `stripe trigger charge.failed`

- **Extra Model Ideas:**  
  - Review, Wishlist, Mailing List, and "How did you hear about us"

- **Font Information (Skia):**  
  - *Skia CC Regular:* `font-family: "skia-cc", sans-serif; font-weight: 400;`  
  - *Skia CC Bold:* `font-family: "skia-cc", sans-serif; font-weight: 700;`  
  - *(Additional variants as needed)*



------------------------------------
NOTES:

Webhook testing: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+BA101N+4/courseware/4201818c00aa4ba3a0dae243725f6e32/09698fc21d8045c79a5d639c90df8cec/?child=first

Stripe Triggers:
stripe trigger payment_intent.created
stripe trigger payment_intent.succeeded
stripe trigger payment_intent.payment_failed
stripe trigger charge.succeeded
stripe trigger charge.failed

Extra model ideas:
Review
Wishlist
Mailing List
How did you hear about us

Scrandit img source:
https://thebristolsauce.substack.com/p/ramen-nakama-the-scrandit-serious

Skia CC Regular
font-family: "skia-cc", sans-serif;
font-weight: 400;
font-style: normal;
Skia CC Bold
font-family: "skia-cc", sans-serif;
font-weight: 700;
font-style: normal;
Skia CC Compressed Regular
font-family: "skia-cc-compressed", sans-serif;
font-weight: 400;
font-style: normal;
Skia CC Compressed Bold
font-family: "skia-cc-compressed", sans-serif;
font-weight: 700;
font-style: normal;
Skia CC Condensed Regular
font-family: "skia-cc-condensed", sans-serif;
font-weight: 400;
font-style: normal;
Skia CC Condensed Bold
font-family: "skia-cc-condensed", sans-serif;
font-weight: 700;
font-style: normal;
Skia CC Semi Condensed Regular
font-family: "skia-cc-semi-condensed", sans-serif;
font-weight: 400;
font-style: normal;
Skia CC Semi Condensed Bold
font-family: "skia-cc-semi-condensed", sans-serif;
font-weight: 700;
font-style: normal;
Skia CC Wide Regular
font-family: "skia-cc-wide", sans-serif;
font-weight: 400;
font-style: normal;
Skia CC Wide Bold
font-family: "skia-cc-wide", sans-serif;
font-weight: 700;
font-style: normal;
Skia CC Extended Regular
font-family: "skia-cc-extended", sans-serif;
font-weight: 400;
font-style: normal;
Skia CC Extended Bold
font-family: "skia-cc-extended", sans-serif;
font-weight: 700;
font-style: normal;