
const express = require('express'); // Mock import
const app = {
    get: (route, callback) => {
        console.log(`[Registered GET ${route}]`);
    },
    post: (route, callback) => {
        console.log(`[Registered POST ${route}]`);
    },
    listen: (port) => {
        console.log(`Server started on port ${port}`);
    }
};

// --- E-Commerce API Simulation ---

const products = [
    { id: 1, name: "Gaming Laptop", price: 1200 },
    { id: 2, name: "Mechanical Keyboard", price: 150 },
    { id: 3, name: "Wireless Mouse", price: 80 }
];

app.get('/api/products', (req, res) => {
    // Return all products
    return products;
});

app.post('/api/checkout', (req, res) => {
    // Simulate payment processing
    console.log("Processing payment...");
    return { status: "success", order_id: Math.floor(Math.random() * 1000) };
});

if (require.main === module) {
    console.log("--- NodeJS E-Commerce API (Mock) ---");
    app.listen(3000);
}
