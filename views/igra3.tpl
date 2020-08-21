%rebase('base.tpl')
%import model

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
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[3]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[4]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(0)[5]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[3]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[4]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(1)[5]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[3]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[4]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(2)[5]}}</td>
  </tr>
  <tr>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[0]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[1]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[2]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[3]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[4]}}</td>
    <td class="tg-ec4q">{{igra.narisi_vrstico(3)[5]}}</td>
  </tr>
</tbody>
</table>

<tr>
  <form action="/igra/" method="post">
    Izberi 1.karto: <input type="numbers" name="izbira1" >
    Izberi 2.karto : <input type="numbers" name="izbira2" >
    Izberi 3.karto : <input type="numbers" name="izbira3" >
    <button type="submit">Ugibaj</button>
  </form>
</tr>


% if stanje == model.ZMAGA:
<p><h1 style="font-size:50px;">Čestitke!</h1></p>
<p><h1 style="font-size:50px;">Zmagal/a si!</h1></p>


<table>
    <tr>
        <td><b>Če želiš igrati še enkrat, ponovno izberi težavnost!</b></td>
    </tr>
    
    <tr>
        <td>
            <form action="/nova_igra/" method="POST">
                <input type="radio" name="tezavnost" value="2"> Lahko<br>
                <input type="radio" name="tezavnost" value="3"> Srednje<br>
                <input type="radio" name="tezavnost" value="3"> Tezko<br>  
                <p><input type="submit" value="prični igro"></p>
            </form>
        </td>
    </tr>
    
</table>
% end 
