const canvas = document.getElementById("revenueChart");

if (canvas) {

    new Chart(canvas, {

        type: "line",

        data: {

            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],

            datasets: [{

                label: "Revenue",

                data: [180000, 230000, 275000, 340000, 390000, 426300],

                borderColor: "#2563eb",

                backgroundColor: "rgba(37,99,235,.15)",

                fill: true,

                tension: .4

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {
                legend: {
                    display: false
                }
            }

        }

    });

}