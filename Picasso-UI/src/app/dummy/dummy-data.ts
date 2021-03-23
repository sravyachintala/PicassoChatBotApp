export const staticJson=
{
    "Response": {
      "status": "success",
      "nlp_tokens": {
        "task": "gross sales",
        "customer": "walmart",
        "category": "breakfast",
        "subcategory": "tea",
        "ppg_id": "123",
        "upc_id": "782364746374",
        "time": "Jan to March"
      },
      "visualization": [
        {
          "type": "numeric_value",
          "value": 10
        },
        {
          "type": "pie_chart",
          "value": {
            "header": "Pie Chart",
            data: [
              {legend: 'Sales',  value: 10},
              {legend: 'Supply Chain',  value: 40},
              {legend: 'Marketing',  value: 20},
              {legend: 'R & D',  value: 30},
            ]
          }
        },
        {
          "type": "table",
          "value": {
            "header": "XYZ",
            data: [
              {
              "columns": [
                "Ranking",
                "Cumulative %"
              ],
              "rows": [
                [
                  "Manufacturing",
                  "35%"
                ],
                [
                  "Sales",
                  "45%"
                ],
                [
                  "Marketing",
                  "20%"
                ]
            ]
            }
          ]
        }
      },
        {
          "type": "bar_chart",
          "value": {
            "header": "Bar Graph",
            "data": [
              {legend: 'Product 1',  value: 10},
              {legend: 'Product 2',  value: 20},
              {legend: 'Product 3',  value: 40},
              {legend: 'Product 4',  value: 60},
              {legend: 'Product 5',  value: 80}
            ]
          }
        }
      ]
    }
  }
  export const SuggestionsJson = [
    "display Max Shipment for Albertsons for meats and bacon in Quarter Q3",
    "display Max Shipment for Albertsons for meats and bacon in Quarter Q3"
  ]