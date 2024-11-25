 <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:strip-space elements="*" />
<xsl:output method="text" indent="no" />
<xsl:template match="/">
{
    "locale": "<xsl:value-of select="/userInfo/locale"/>",
    "first_name": "<xsl:value-of select="/userInfo/first_name"/>",
    "last_name": "<xsl:value-of select="/userInfo/last_name"/>",
    "dob": "<xsl:value-of select="/userInfo/dob"/>",
    "tin": "<xsl:value-of select="/userInfo/tin"/>",
    "phone_number": "<xsl:value-of select="/userInfo/phone_number"/>",
    "address":{
        "street": "<xsl:value-of select="/userInfo/address/street"/>",
        "city": "<xsl:value-of select="/userInfo/address/city"/>",
        "state": "<xsl:value-of select="/userInfo/address/state"/>",
        "zip_code": "<xsl:value-of select="/userInfo/address/zip_code"/>"
    }
}
 </xsl:template>
</xsl:stylesheet>