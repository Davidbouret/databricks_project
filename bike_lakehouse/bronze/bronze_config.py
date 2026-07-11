BASE_PATH = "/Volumes/workspace/bronze/source_systems"

INGESTION_CONFIG = [

    #CRM
    {
        "source": "crm",
        "path": f"{BASE_PATH}/cust_info.csv",
        "table": "crm_cust_info"

    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/prd_info.csv",
        "table": "crm_prd_info"

    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/sales_details.csv",
        "table": "crm_sales_details"

    },

    #ERP
    {
        "source": "erp",
        "path": f"{BASE_PATH}/CUST_AZ12.csv",
        "table": "erp_cust_az12"

    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/LOC_A101.csv",
        "table": "erp_loc_a101"

    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/PX_CAT_G1V2.csv",
        "table": "erp_px_cat_g1v2"

    },
]

