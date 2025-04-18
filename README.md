# ferry_booking_system
An object-oriented ferry booking system written in Python, demonstrating key software design principles.

## My FerryBookingSystem & Software Design Principles
As the developer of this FerryBookingSystem, I aimed to create a simple, functional, and user-friendly booking program. While building it, I tried to keep best practices in mind, particularly core software design principles. Below is how each principle relates to my code:

## KISS (Keep It Simple, Stupid)
In this project, I kept my logic straightforward and easy to follow. For example, the program is written mostly within one method, run_booking_system(), where users are prompted for their ID, name, items, and approval. This linear, no-frills structure makes it easy to understand what's happening step-by-step.

However, I realize that having everything inside one method might make the code harder to manage as it grows. If I were to make this system more complex—say, adding online payments or passenger types—I’d definitely break the code into smaller methods. That way, it would still stay simple but become more maintainable.
## DRY (Don’t Repeat Yourself)
Right now, some parts of my code repeat logic. For instance, I print booking details more than once (both during input and again in the summary), and I ask for multiple inputs using the same structure without reusing a function. If I wanted to improve this, I could refactor those sections into functions like get_passenger_info() or display_summary(). This would reduce repetition and make updates easier in the future.

## Open/Closed Principle
At the moment, my code is not fully following this principle. If I want to add new features—like support for multiple ticket types or a discount system—I would have to go into the existing method and modify it, which goes against the “closed for modification” idea.

If I refactored it into smaller functions or even additional classes (like a Passenger class or a Booking class), I could extend the system by adding new features without changing the core logic.

## Composition Over Inheritance
I didn’t use inheritance in this system, which is actually good in this case! Instead, I stuck with a single class and procedural logic. If I were to expand this system, I would prefer composition—like building helper classes for specific tasks (e.g., a Receipt class for handling pricing and approval)—so I can plug those into the main system when needed.

## Single Responsibility Principle
Right now, my FerryBookingSystem class is doing a bit too much. It:

Takes user input

Calculates totals

Manages approvals

Prints summaries

That’s a lot of responsibility for one function! Ideally, each of these should be handled by separate methods or even classes. That way, if something breaks—say, the price calculation—it wouldn’t affect the rest of the system. It also makes it easier to fix or upgrade one part without touching everything else.

## Separation of Concerns
Currently, all concerns (input, processing, display) are mashed together in run_booking_system(). This works for a basic version, but for better structure, I should separate these concerns.

For example:

A method just for taking user input

One for calculating the total cost

Another to handle approvals and reference numbers

A method to print the booking summary

This would make the system easier to debug and improve later.

## YAGNI (You Aren’t Gonna Need It)
I followed this principle well! I didn’t add any future-proofing or unnecessary features. I only built what I needed to make a functioning booking system—nothing extra like account systems, online syncing, or seat selection. This helped me keep the code focused and avoid wasting time on features that aren’t required yet.

## Avoid Premature Optimization
I didn’t try to optimize things too early, either. Instead of over-engineering my calculations or approval process, I made sure it was correct first. My priority was readability and reliability, and only once performance becomes a problem (like handling hundreds of bookings), I would consider improving performance.

## Refactor, Refactor, Refactor
While I haven’t fully refactored yet, I’m very aware that my current setup would benefit a lot from some refactoring. If I break out parts of the code into helper functions or classes, I can improve clarity and reduce repetition. Refactoring regularly would also allow me to improve efficiency without changing how the system behaves from the user’s point of view.

## Clean Code > Clever Code
I made sure my code is readable and logical rather than clever. I avoided one-liners or tricky expressions that might look cool but confuse someone else reading it—or even confuse me later. Instead, I chose to use plain, understandable variable names (form_of_id, ticket_id, passenger_name) and clear step-by-step logic.

## Final Thoughts
Overall, while my current version of the FerryBookingSystem works and follows some principles like KISS, YAGNI, and Clean Code, it still has room to improve when it comes to DRY, Single Responsibility, and Separation of Concerns. With a bit of refactoring and class restructuring, I could bring the code even closer to professional-level software design standards.
