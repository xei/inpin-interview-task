package com.xei.inpin


import com.google.gson.annotations.SerializedName

data class Message(
    @SerializedName("msg")
    val msg: String,
    @SerializedName("status")
    val status: Boolean
)