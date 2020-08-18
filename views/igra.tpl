%rebase('base.tpl')
%import model



 

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:50px 50px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-ec4q{font-size:xx-large;text-align:center;vertical-align:middle}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<tbody>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[3]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[3]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[3]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[3]}}</td>
  </tr>
</tbody>
</table>

<tr>
  <form action="/igra/" method="post">
    Izberi karte : <input type="numbers" name="izbira" >
    <button type="submit">Ugibaj</button>
  </form>
</tr>

</table>

 