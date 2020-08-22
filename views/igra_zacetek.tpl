%rebase('base.tpl')
%import model

<h1 style='text-align: center;
  text-transform: uppercase;
  color: #800000;Vfont-size:60px;' ><b>SPOMIN</b></h1>

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:45px 45px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-ec4q{font-size:xx-large;text-align:center;vertical-align:middle}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<tbody>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(0)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(0)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(0)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(0)[3]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(1)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(1)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(1)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(1)[3]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(2)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(2)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(2)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(2)[3]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(3)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(3)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(3)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico_zacetek(3)[3]}}</td>
  </tr>
</tbody>
</table>

<tr>
  <form action="/pricni_igro/" method="post">
    <p><input type="submit" value="začni z ugibanjem" ></p>
  </form>
</tr>

</table>
