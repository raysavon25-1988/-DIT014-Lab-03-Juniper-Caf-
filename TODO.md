# Juniper Café — TODO

## Current Status

Lab 03 is in progress.

Implemented:
- [x] Available tables (1–20)
- [x] Ask for table number
- [x] Check whether table exists
- [x] Ask for client name
- [x] Display client name in uppercase
- [x] Store café products
- [x] Store corresponding product prices
- [x] Display menu using a `for` loop and indexes
- [x] Display prices with two decimal places
- [x] Calculate a subtotal from three prices
- [x] Git repository connected to GitHub

## Next Session

### 1. Finish menu presentation
- [ ] Change `JUPITER MENU` to `JUNIPER MENU`
- [ ] Improve product/price alignment
- [ ] Add take-away charge below the normal menu

### 2. Improve product selection
- [ ] Customer selects products from the existing menu
- [ ] Avoid asking the customer to manually enter known prices
- [ ] Connect selected product to its corresponding price
- [ ] Keep menu products separate from ordered products
- [ ] Do not overwrite the original `products` list

### 3. Take-away
- [ ] Ask whether the order/product is take-away
- [ ] Define the exact take-away pricing rule
- [ ] Add the charge only when applicable
- [ ] Include the charge in the subtotal
- [ ] Show it clearly on the receipt

### 4. Complete receipt
- [ ] Display table number
- [ ] Display uppercase client name
- [ ] Display three selected products
- [ ] Display corresponding prices
- [ ] Align product names and prices
- [ ] Display take-away charge when applicable
- [ ] Display calculated subtotal

### 5. Input validation
- [ ] Invalid table should not continue as valid program state
- [ ] Investigate non-numeric table input
- [ ] Test invalid product selections

### 6. Testing
- [ ] Run official Lab 03 example
- [ ] Predict subtotal before execution
- [ ] Compare expected vs observed result
- [ ] Run second dataset
- [ ] Test take-away order
- [ ] Test non-take-away order
- [ ] Test invalid inputs

### 7. Lab 03 mastery check
- [ ] Explain `input()` and returned types
- [ ] Explain numeric conversion
- [ ] Explain stored value vs formatted value
- [ ] Explain `.2f`
- [ ] Explain indexing
- [ ] Explain slicing
- [ ] Explain negative indexing
- [ ] Explain why some numeric-looking identifiers remain strings

## Git Workflow

After each meaningful milestone:

1. `git status`
2. `git diff`
3. Test the program
4. `git add <file>`
5. `git commit -m "meaningful message"`
6. `git push`

## Definition of Done

Lab 03 is complete when:

- [ ] Official Lab 03 requirements are satisfied
- [ ] Juniper Café extension works
- [ ] Required tests pass
- [ ] I can explain the important concepts without running the code
- [ ] Final code and documentation are pushed to GitHub