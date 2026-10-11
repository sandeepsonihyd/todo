# Plan: Client-side Category Filter for Todo List

Add a dropdown above the todo list that filters the already-fetched todos by category, entirely client-side in React state. No backend changes.

**Steps**
${input:var}
1. In `frontend/src/App.jsx`: add `const [selectedCategory, setSelectedCategory] = useState('all')` state.
2. Derive a filtered list: `const filteredTodos = selectedCategory === 'all' ? todos : todos.filter(t => t.category === selectedCategory)`. Pass `filteredTodos` to `<TodoList />` instead of `todos`.
3. Add a `<select>` control above `<TodoList />` (in the JSX returned by `App.jsx`) with an "All" option plus one `<option>` per entry in `CATEGORIES` from `frontend/src/constants/categories.js`. `onChange` sets `selectedCategory`.
4. No changes needed to `frontend/src/api/todoApi.js`, `TodoList.jsx`, `TodoItem.jsx`, or backend files — filtering happens purely on the in-memory `todos` state after fetch.

**Relevant files**
- `frontend/src/App.jsx` — add `selectedCategory` state, derived `filteredTodos`, and the filter `<select>` UI above `TodoList`
- `frontend/src/constants/categories.js` — reuse existing `CATEGORIES` array (`['official', 'personal', 'general']`) to populate dropdown options

**Verification**
1. Run frontend dev server (`npm run dev` in `frontend/`), confirm dropdown appears above the list with "All" + 3 categories.
2. Create todos in different categories, verify selecting a category shows only matching todos, and "All" shows everything.
3. Confirm toggling completion / editing / deleting still works correctly while a filter is active.

**Decisions**
- Filtering is client-side only per user choice — simpler, no backend/API changes, acceptable since todo list is small (in-memory demo app).
- Scope excludes backend query-param filtering (`GET /api/todos?category=`) — deliberately out of scope.
