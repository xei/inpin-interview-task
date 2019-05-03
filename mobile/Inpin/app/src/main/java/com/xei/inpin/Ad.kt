package com.xei.inpin


import com.google.gson.annotations.SerializedName

data class Ad(
    @SerializedName("agency_id")
    val agencyId: Int,
    @SerializedName("name")
    val name: String,
    @SerializedName("latitude")
    val latitude: Double,
    @SerializedName("longitude")
    val longitude: Double
)