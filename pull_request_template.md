_Replace this text with a description of **what** your changes actually do, and the **motivation** behind them._

## Pull Request Style Guide
- [ ] Title starts with `ASKAI-` issue code.
- [ ] Title uses imperative form.
- [ ] Sufficient description is included. (Lack of a good description should be a valid reason to reject a pull request)
- Work-in-progress pull requests should be created as a github "draft" pull request.

## Author's duties
- [ ] I have reviewed this code myself, adding comments and remarks where necessary.
- [ ] I have added all necessary labels.
- The author is responsible for **answering** all conversations on the pull request before merging. That the conversation shows "outdated" is not an accepted answer. The only exception is "nit" comments; they need not be answered.
- The author is responsible for making sure their code is reviewed **within one (1) business day**.
- If a conversation is started about unclear code, either **refactor** the affected part(s), or include a summary of the conversation as a **comment in the code**.
- If a conversation is started about over-engineered code, the author is responsible for explaining why the code is not over-engineered.
- When making fixes to an already approved pull request, the author should never introduce _major_ new functionality. If they do, a review should be re-requested.

## Reviewer's duties
- [ ] I have assigned myself to this pull request.
- Approve a pull request when you feel all _major_ issues have been resolved, or you are certain that the author will apply your suggestions before merging.
- Prefix less important comments with `nit:` to signal that they are not necessary for approval.
- The reviewer is responsible for **resolving** all conversations started by themselves. 
- Try to figure out if the code seems sensible to you as an end-user of the app.
- If the structure of the pull request makes it hard to understand, the reviewer can:
    1. Review the test code before moving on to the main code.
    2. Ask the author for a better description, and/or where to start reviewing.
    3. Ask the author for an order in which files should be reviewed.
    4. Ask the author to split up the pull request.

---

###### All guidelines are based on our [Code Review Best Practices] .
