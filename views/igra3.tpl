%rebase('base.tpl')
%import model

<div class="row">
  <div class="column left" style="background-color:#d2a679;">
    <h2>Pomoč:</h2>
    <p>Karto izbereš tako da vpišeš njene kordinate. Najprej vpišeš vrstico(med 0 in 3), nato pa stolpec(med 0 in 5).
    Primer: Izberi 1.karto: 21 Izberi 2.karto: 03 Izberi 3.karto: 35. Nato pritisni gumb Ugibaj ali enter.</p>
    <h2>Izberi polja:</h2>
    <form action="/igra/" method="post">
      <p>Izberi 1.karto: <input type="numbers" name="izbira1" ></p>
      <tr>
      <p>Izberi 2.karto : <input type="numbers" name="izbira2" ></p>
      </tr>
      <p>Izberi 3.karto : <input type="numbers" name="izbira3" ></p>
      <button type="submit">Ugibaj</button></tr>
    </form>

    <h3>Če želite pričeti novo igro ponovno izberite težavnost:</h3>
    
    <tr>
        <td>
            <form action="/nova_igra/" method="POST">
                <input type="radio" name="tezavnost" value="1"> Lahko<br>
                <input type="radio" name="tezavnost" value="2"> Srednje<br>
                <input type="radio" name="tezavnost" value="3"> Tezko<br>  
                <p><input type="submit" value="prični novo igro"></p>
            </form>
        </td>
    </tr>
  </div> 

  <div class="column right" style="background-color:#ffffff;">
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
        <th></th> 
        <th>0</th> 
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
      </tr>
    
      <tr>
        <th>0</th>
        <td class="tg-ec4q">{{igra.narisi_vrstico(0)[0]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(0)[1]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(0)[2]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(0)[3]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(0)[4]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(0)[5]}}</td>
      </tr>
      <tr>
        <th>1</th>
        <td class="tg-ec4q">{{igra.narisi_vrstico(1)[0]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(1)[1]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(1)[2]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(1)[3]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(1)[4]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(1)[5]}}</td>
      </tr>
      <tr>
        <th>2</th>
        <td class="tg-ec4q">{{igra.narisi_vrstico(2)[0]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(2)[1]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(2)[2]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(2)[3]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(2)[4]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(2)[5]}}</td>
      </tr>
      <tr>
        <th>3</th>
        <td class="tg-ec4q">{{igra.narisi_vrstico(3)[0]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(3)[1]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(3)[2]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(3)[3]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(3)[4]}}</td>
        <td class="tg-ec4q">{{igra.narisi_vrstico(3)[5]}}</td>
      </tr>
    </tbody>
    </table>
</div> 
</div>
 
