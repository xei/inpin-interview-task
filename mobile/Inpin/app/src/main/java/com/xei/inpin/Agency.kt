package com.xei.inpin


import com.google.gson.annotations.SerializedName

data class Agency(
    @SerializedName("id")
    val id: Int,
    @SerializedName("name")
    val name: String,
    @SerializedName("parent_id")
    val parentId: Int
)