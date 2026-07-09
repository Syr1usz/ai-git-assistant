<?php

class Koszyk
{
    private array $produkty = [];
    private float $suma = 0.0;

    public function dodajProdukt(string $nazwa, float $cena): void
    {
        $this->produkty[] = $nazwa;
        $this->suma += $cena;
    }

    public function iloscProduktow(): int
    {
        return count($this->produkty);
    }

    public function obliczSume(): float
    {
        return $this->suma;
    }
}